from invoke import task, Collection

from metapack_build.tasks.collection import ns, foreach_metapack_subdir

@task
def reset_tasks(c):
    """Reset the tasks.py file in each subdirectory"""
    
    for d in foreach_metapack_subdir():
        c.run('rm tasks.py')
        c.run('mp update -f')

@task
def print_package_urls(c):
    """Print the package url for each sub directory"""
    
    for d in foreach_metapack_subdir():
        c.run('mp info -p')



ns.add_task(reset_tasks)
ns.add_task(print_package_urls)