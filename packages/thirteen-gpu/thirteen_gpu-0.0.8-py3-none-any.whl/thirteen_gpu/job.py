

from .definition import JobStatus, WORKSPACE_DIR
from .ssh import SSH
from .worker import GPU, Worker


def get_running_sessions(workers: list):
    running_jobs = []
    
    for worker in workers:
        running_jobs += worker.get_running_sessions()
    
    return running_jobs

class Job(object):
    def __init__(self, project_name, job_name, user, config_path, id=0):
        
        self.status = JobStatus.PENDING
        self.project_name = project_name
        self.job_name = job_name
        self.config_path = config_path # config/runs/xxx.json
        self.user = user
        self.job_id = id        
        
        self.worker = None
        self.session_name = ""
    
    def run(self, worker: Worker, gpu: GPU):
                
        # project code 를 worker 로 복사
        worker.ssh.ssh_copy(
            src=f"{WORKSPACE_DIR}/{self.project_name}",
            dst=f"{worker.home}/{self.project_name}/"
        )
                
        REMOTE_WORKSPACE_DIR = f"{worker.home}/{self.project_name}"
        
        command = \
            f"test -e {REMOTE_WORKSPACE_DIR}/data || ln -s /data {REMOTE_WORKSPACE_DIR}/ && " + \
            f"export AWS_ACCESS_KEY_ID=AKIAXCPLIY4KT76BUDF4 && " + \
            f"export AWS_SECRET_ACCESS_KEY=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 && " + \
            f"export AWS_S3_BUCKET=thirteen-ai && " + \
            f"export CUDA_VISIBLE_DEVICES={gpu.gpu_id} && " + \
            f"source $HOME/.miniconda3/bin/activate && " + \
            f"cd {REMOTE_WORKSPACE_DIR} && " + \
            f"echo 'running' > {REMOTE_WORKSPACE_DIR}/{self.job_name}.status && " + \
            f"(python train.py {self.config_path} && echo 'finished' > {REMOTE_WORKSPACE_DIR}/{self.job_name}.status) || echo 'failed' > {REMOTE_WORKSPACE_DIR}/{self.job_name}.status"
            
        # tmux session 으로 job 실행
        self.session_name = f"gpu{gpu.gpu_id}_{self.job_name}"
        
        worker.ssh.ssh_exec_command(f"tmux new-session -s {self.session_name} -d '{command}'")                
        
        print(f"Job {self.job_name} is running on {gpu.ip}:{gpu.port} (gpu: {gpu.gpu_id})")
    
        self.status = JobStatus.RUNNING
        
        self.worker = worker
            
    def stop(self):
        self.worker.ssh.ssh_exec_command(
            f"tmux kill-session -t {self.session_name} && echo 'stopped' > {self.worker.home}/{self.project_name}/{self.job_name}.status"
        )
        
        self.status = JobStatus.STOPPED
        
    
