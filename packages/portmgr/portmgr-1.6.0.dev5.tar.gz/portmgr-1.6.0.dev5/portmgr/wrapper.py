import json
import os
from subprocess import call


def getServices(includeOnlyBuildable=False):
    data = call(['docker', 'compose', 'config', '--format', 'json'])
    config = json.loads(data)
    services = config['services']
    if includeOnlyBuildable:
        services = [s for s in services if 'build' in s.keys()]
    return services


def getServicesRunning():
    data = call(['docker', 'compose', 'ps', '--format', 'json'])
    container_list = json.loads(data)
    container_names = [s['name'] for s in container_list]
    return container_names


def getImages():
    data = call(['docker', 'compose', 'images', '--format', 'json'])
    image_list = json.loads(data)
    images = [
        {'ID': image['ID'],
         'Name': image['Repository'],
         'ContainerName': image['ContainerName'],
         'Tag': image['Tag']}
        for image in image_list
    ]
    return images


def getStats():
    containers = getServicesRunning()
    data = call(['docker', 'stats', '--format', 'json', '--no-stream'] + containers)
    stats = json.loads(data)
    return stats


def runCompose(args, **kwargs):
    command = ['docker', 'compose']
    if os.environ.get("PORTMGR_IN_SCRIPT", "").lower() == "true":
        command += ["--ansi", "never"]
    command += list(args)
    return call(command, **kwargs)
