import dataclasses

import pkg_resources
import requests
import json
from distutils.version import StrictVersion
from dataclasses import dataclass

this_version = pkg_resources.get_distribution('mattuni').version



# https://stackoverflow.com/a/27239645/6596010
def versions(package_name):
    url = "https://pypi.org/pypi/%s/json" % (package_name,)
    data = json.loads(requests.get(url).text)
    versions = list(data["releases"].keys())
    versions.sort(key=StrictVersion)
    return versions


online_versions = versions("mattuni")
latest_version = online_versions[len(online_versions) - 1]
if (this_version != latest_version):
    print(
        f"WARNING: You are using mattuni {this_version} but the latest version is {latest_version}. In the terminal use `python -m pip install mattuni --upgrade` to update.")

_ran_x_times = []


_url_prefix = 'https://teach-anya.herokuapp.com'


@dataclass
class Challenge:
    number: int

    def __post_init__(self):
        self.req = str.encode(json.dumps({
            "q": self.number,
        }))

    def prompt(self):
        response = requests.get(f'{_url_prefix}/prompt', data=self.req)
        print(response.text)


    def input(self):
        print(f"Getting json input for question {self.number} ...")
        response = requests.get(f'{_url_prefix}/get-big-input', data=self.req)
        r = response.text
        print(f"Got json input (number of characters={len(response.text)}) Don't forget to decode it!")
        return r


    def send_answer(self,answer):
        print()
        print()
        global _ran_x_times
        if self.number in _ran_x_times:
            print(f"Challenge {self.number} Failed. You can only call send_answer one time per challenge.")
        else:
            _ran_x_times.append(self.number)
            if (len(answer) < 200):
                print(f"Sending answer for question {self.number}: \"" + answer + "\" ...")
            else:
                print(f"Sending the (very long) answer for question {self.number}...")
            j = json.dumps({
                "q": self.number,
                "answer": answer
            })
            response = requests.get(f'{_url_prefix}/send', data=str.encode(j))
            print(response.text)
            print()
            print()


