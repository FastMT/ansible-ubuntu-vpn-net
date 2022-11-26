###########################################################
#
# Convert Wireguard private key to public
# Usage:
# - debug:
#     msg: "{{ 'iE/GAabZwQZ0dK5r2PgjwVNXpGPl/swCu+c+bZup628=' | wg_pubkey }}"
#

import subprocess

def wg_genkey(a: str):
    pubkey = subprocess.check_output(["wg", "genkey"])
    pubkey_cleaned = pubkey.decode("utf-8").strip()
    return pubkey_cleaned

def wg_pubkey(a: str):
    pipe = subprocess.Popen(["echo", a], stdout=subprocess.PIPE)
    pubkey = subprocess.check_output(
        ["wg", "pubkey"], stdin=pipe.stdout)
    pubkey_cleaned = pubkey.decode("utf-8").strip()
    return pubkey_cleaned

class FilterModule(object):
    ''' WireGuard filters '''

    def filters(self):
        return {
            # jinja2 overrides
            'wg_genkey': wg_genkey,
            'wg_pubkey': wg_pubkey

        }