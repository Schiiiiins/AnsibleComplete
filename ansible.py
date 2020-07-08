import ansible_runner
import os


def ansible_playbook(user_input):
    r = ansible_runner.run(data_dir=os.getcwd(), playbook=user_input)
    print("{}: {}".format(r.stats, r.rc))
    for each_host_event in r.events:
        print(each_host_event['event'])
    print("Final status: ")
    print(r.stats)
