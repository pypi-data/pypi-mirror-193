from collections import defaultdict
import json
import os
from .definition import JobStatus
from .ssh import SSH


def get_available_gpus_across_workers(workers):
    
    for worker in workers:
        worker_available_gpus = worker.get_available_gpus()
        
        # 첫번째 available gpu 반환
        if len(worker_available_gpus) > 0:
            return worker_available_gpus[0]
    
    # available gpus 가 모든 workers 에 없으면 빈 리스트 반환
    return []


class Worker(object):
    def __init__(self, name, ip, port, user, n_gpus, home):
        self.name = name
        self.ip = ip
        self.port = port
        self.user = user
        self.n_gpus = n_gpus
        self.home = home
        
        self.ssh = SSH(ip, port, user)
    
        self.max_jobs_per_gpu = 2
            
    def get_available_gpus(self):
        """ job 이 `max_jobs_per_gpu` 개 이하로 사용 중인 gpu 목록 반환한다 """
        
        gpu_usage = {gpu: 0 for gpu in range(self.n_gpus)}
        
        # tmux session 이름들을 가져오기
        sessions = self.ssh.ssh_exec_command(
            f"tmux ls | cut -d ':' -f 1"
        )
        
        # session 이름으로부터 사용중인 GPU 개수 카운팅
        for session_name in sessions.split("\n"):
            if session_name.startswith("gpu"):
                gpu_id = int(session_name.split("_")[0].replace("gpu", ""))
                gpu_usage[gpu_id] += 1

        # 사용 중인 gpu 제외하고 남은 gpu 반환
        available_gpus = []
        for gpu_id in range(self.n_gpus):
            
            for count in range(self.max_jobs_per_gpu - gpu_usage[gpu_id]):
                available_gpus.append(GPU(self.ip, self.port, self.user, gpu_id))
                
        return available_gpus
    
    def get_running_sessions(self):
        sessions = self.ssh.ssh_exec_command(
            f"tmux ls | cut -d ':' -f 1"
        ).split("\n")
        
        sessions = [session for session in sessions if session.startswith("gpu")]
                     
        return sessions
    
    def update_job_status(self, projects: list):
        """ Worker 안에서 실행되는 모든 프로젝트의 job 들의 상태를 업데이트한다 """                
        
        # read */*.status files with filename format: job_{job_name}.status
        
        job_names = [
            os.path.basename(status_fname).split(".status")[0] 
            for status_fname in self.ssh.ssh_exec_command("ls */*.status").split("\n")
        ][:-1]
        
        status_values = self.ssh.ssh_exec_command(
            f"cat */*.status"
        ).split("\n")[:-1]
        
        try:
            assert len(job_names) == len(status_values)
        except:
            from IPython import embed; embed(header="job_names, status_values length mismatch")
                
        for job, status_value in zip(job_names, status_values):
            for project in projects:
                if job in project.jobs:
                    
                    if status_value == "running":                        
                        project.jobs[job].status = JobStatus.RUNNING
                    elif status_value == "finished":
                        project.jobs[job].status = JobStatus.SUCCESS
                    elif status_value == "failed":
                        project.jobs[job].status = JobStatus.FAILED
                    else:
                        from icecream import ic; ic(job, status_value)
                        from IPython import embed; embed()
                        project.jobs[job].status = JobStatus.UNKNOWN
                                       
        # write job status to txt file
        with open(f"thirteen_gpu/status.json", "w") as f:
            status = defaultdict(lambda: defaultdict(int))            
            
            for project in projects:
                # initialize status dict (dict of dict of int) 
                status[project.project_name]["user"] = project.user
                status[project.project_name]["submit_at"] = project.submit_at
                status[project.project_name]["status"] = defaultdict(int)
                
                for job in project.jobs.values():
                    status[project.project_name]["status"][job.status.name] += 1
                
                # dump to json file
            json.dump(status, f, indent=4)
                
                
                    
class GPU(object):
    def __init__(self, ip, port, user, gpu_id):
        self.ip = ip
        self.port = port
        self.user = user
        self.gpu_id = gpu_id
