#job scheduler
#build a graph of jobs and edges between jobs and their dependent jobs

#iterate thru all nodes
#schedule a job only if can be run (meaning it shouldnt have any dependencies or all the dependencies are already have run)
#if job has dependent jobs then schedule them (recursive call)
#finally schedule this job


finished_jobs = []

def get_dependency(job):
    
    return job_graph[job]


def can_run(job):
    
    for dependency_job in job_graph[job]:
        if dependency_job not in finished_jobs:
            return False
        
    return True


def check_circular_dependency(job):
    for dependency_job in job_graph[job]:
        dependency_jobs = job_graph[dependency_job]
        if job in dependency_jobs:
            return True
        
    
    return False


def schedule(job):
    
    if check_circular_dependency(job):
        print "job " + str(job) + " cannot be run because of cicular dependency"
        return
       
    if can_run(job):
        #print job
        finished_jobs.append(job)
        return
    
    for dependency in job_graph[job]:
        schedule(dependency)
    schedule(job)
        

if __name__ == "__main__":
    
    job_graph = {7:[8], 8:[], 1:[2], 2:[3,4], 3:[5], 4:[], 5:[], 6:[]}
    #job_graph = {1:[2], 2:[1]}
    for job in job_graph.keys():
        if job in finished_jobs:
            continue
        schedule(job)
    
    
    print finished_jobs
        
        
        
