
finished_jobs = []

def get_dependency(job):
    
    return job_graph[job]


def can_run(job):
    
    for dependency_job in job_graph[job]:
        if dependency_job not in finished_jobs:
            return False
        
    return True


def schedule(job):
       
    if can_run(job):
        #print job
        finished_jobs.append(job)
        return
    
    dependency = job_graph[job]
    for job_d in dependency:
        schedule(job_d)
    schedule(job)
        

if __name__ == "__main__":
    job_graph = {7:[8], 8:[], 1:[2], 2:[3,4], 3:[5], 4:[], 5:[], 6:[]}
    for job in job_graph.keys():
        job in finished_jobs:
            continue
        schedule(job)
    
    print finished_jobs
        
        
        
