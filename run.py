import subprocess
import csv
import re

GP_BASIC_COMMAND = 'gp.exe'  # command which will start GlobalPlatformPro binary
GP_AUTH_FLAG = ''  # most of the card requires no additional authentication flag
# GP_AUTH_FLAG = '--emv'  # use of EMV key diversification is used (e.g., G&D cards)


def best_match_rid(aid, rid_list):
    for rid_ctx in rid_list:
        if len(rid_ctx) > 0:
            if aid.startswith(rid_ctx[0]):
                return "{0}, Vendor: {1} / {2}".format(rid_ctx[0], rid_ctx[1], rid_ctx[2])

    return "unknown RID"


def best_match_aid(aid, aid_list):
    for aid_ctx in aid_list:
        if len(aid_ctx) > 0:
            if aid == aid_ctx[0]:
                return "{0}, {1}, Vendor: {2} / {3}".format(aid_ctx[3], aid_ctx[4], aid_ctx[1], aid_ctx[2])

    return "unknown AID"


def gp_list():
    # load list of well-known aids and rids
    # taken from https://www.eftlab.co.uk/index.php/site-map/knowledge-base/211-emv-aid-rid-pix
    # and https://www.eftlab.co.uk/index.php/site-map/knowledge-base/212-emv-rid
    with open('well_known_aids.csv', 'r') as f:
        reader = csv.reader(f)
        aid_list = list(reader)

    # strip leading/trailing zeroes
    for aid_ctx in aid_list:
        for name in aid_ctx:
            name.strip()

    with open('well_known_rids.csv', 'r') as f:
        reader = csv.reader(f)
        rid_list = list(reader)

    # strip leading/trailing zeroes
    for rid_ctx in rid_list:
        for name in rid_ctx:
            name.strip()

    # run gp and get list of applets
    result = subprocess.run([GP_BASIC_COMMAND, GP_AUTH_FLAG, '--list'], stdout=subprocess.PIPE)
    result_text = result.stdout.decode("utf-8")
    gp_lines = result_text.splitlines()

    # print gp result in augmented mode 'AID info:'
    for line in gp_lines:
        match = re.match(r'AID: (?P<aid>.*?) \(', line, re.I)
        if match:
            # AID in output detected
            print(line)
            # annotate (if known)
            print("     RID info: {0}".format(best_match_rid(match.group("aid"), rid_list)))
            print("     AID info: {0}".format(best_match_aid(match.group("aid"), aid_list)))
        else:
            # other lines from gp - just print
            print(line)


def main():
    gp_list()


if __name__ == "__main__":
    main()

