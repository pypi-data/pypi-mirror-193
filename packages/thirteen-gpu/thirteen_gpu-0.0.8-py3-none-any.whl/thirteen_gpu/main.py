from glob import glob
import json
import os
from pprint import pprint
from time import sleep

from .definition import JobStatus, ProjectStatus, WORKSPACE_DIR
from .worker import Worker
from .project import Project


def main():
            
    # workers 정보 가져오기
    workers_info = json.load(open('thirteen_gpu/workers.json'))
    workers = [Worker(**worker_info) for worker_info in workers_info.values()]
    
    projects = []
    
    first_iteration = True
    while True:
        
        sleep(10)
        
        # 유저가 제출한 프로젝트 목록 가져오기 (시간 순 정렬)
        # `project_path` = /path/to/workspace/username_projectname
        new_projects = []
        for project_path in glob(f"{WORKSPACE_DIR}/*"):
            user = open(f"{project_path}/user.txt").read().strip()
            submit_at = open(f"{project_path}/submit_at.txt").read().strip()
            
            new_projects.append(Project(project_path, user, submit_at))
        
        new_projects = sorted(new_projects, key=lambda x: x.submit_at)
        
        # 추가된 project
        for new_project in new_projects:
            if new_project.project_name not in [project.project_name for project in projects]:
                projects.append(new_project)
                
        # 최근의 Job Status Loading
        if first_iteration:
            first_iteration = False
            
            # 각 worker 들에 존재하는 *.status 파일들을 읽어옴
            job_names, status_values = [], []
            for worker in workers:
                job_names.extend([
                    os.path.basename(job).replace(".status", "") 
                    for job in worker.ssh.ssh_exec_command("ls */*.status").split("\n")
                ])
                
                status_values.extend(
                    worker.ssh.ssh_exec_command(f"cat */*.status").split("\n")
                )
            
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
                            project.jobs[job].status = JobStatus.UNKNOWN
                        
                        print(f"[Loading] Assign Status of Job {job} to {project.jobs[job].status}")
                        break
                                      
        # 메모리로 관리하는 projects 가 있는데, 디스크에는 없으면 삭제된 것으로 간주함
        deleted_projects = []
        for project in projects:   
            if project.project_name not in [new_project.project_name for new_project in new_projects]:
                deleted_projects.append(project)
                                                
        deleted_jobs = [job.job_name for project in deleted_projects for job in project.jobs.values()]
            
        print(f"projects: {[project.project_name for project in projects]}")

        if len(deleted_projects) > 0:
            
            # worker 마다 deleted job 에 해당하는 container 중지
            for worker in workers:
                                    
                # running jobs 목록 가져오기
                running_sessions = worker.get_running_sessions()

                # Running 중인 Job 인데, deleted project 목록에 있으면 stop
                stopping_sessions = []
                for session in running_sessions:
                    # session_name -> gpuX_jobname
                    # job_name -> jobname
                    job_name = "_".join(session.split("_")[1:])
                    if job_name in deleted_jobs:
                        stopping_sessions.append(session)                           

                if len(stopping_sessions) > 0:
                    pprint(f"{worker.name} 에서 중지할 job: {stopping_sessions}")
                    command = ""
                    for session in stopping_sessions:
                        command += f"tmux kill-session -t {session};"
                    worker.ssh.ssh_exec_command(command)
            
            for project in deleted_projects:
                project.delete()
                
                for job in project.jobs.values():
                    job.status = JobStatus.STOPPED
        
        # projects 를 job 단위로 분리
        jobs = []
        for project in projects:
            if project.status.value != ProjectStatus.LIVE.value:
                continue
            
            for job in project.jobs.values():
                if job.status.value == JobStatus.PENDING.value:
                    jobs.append(job)
                
        # 사용 가능한 GPU 를 가져오고, Waiting 상태인 최상단 job 을 실행
        available_gpus = []
        for worker in workers:
            for gpu in worker.get_available_gpus():
                available_gpus.append((worker, gpu))  
                
        with open("available_job_slots.txt", "w") as f:
            f.write(str(len(available_gpus)))                  
        
        if len(jobs) > 0 and len(available_gpus) > 0:            
            for job, (worker, gpu) in zip(jobs, available_gpus):                                
                job.run(worker, gpu)
            
        else:            
            if len(jobs) == 0:
                print("No pending job")
                
            if len(available_gpus) == 0:
                print("No available GPU")
        
        # Job status 업데이트
        for worker in workers:
            worker.update_job_status(projects=projects)
                    
        # 특정 Project 의 모든 Job 이 끝난 상태면, Project 폴더 삭제        
        projects_done = []
        for project in projects:
            if project.status.value == ProjectStatus.DEAD.value:
                continue 
            
            if all([
                job.status in (JobStatus.SUCCESS, JobStatus.FAILED, JobStatus.CRASHED, JobStatus.STOPPED, JobStatus.UNKNOWN) 
                for job in project.jobs.values()]
            ):
                print(f"Delete project {project.project_name}")
                project.delete()
        
        print('-' * 80)
                                                
if __name__ == '__main__':
    main()
