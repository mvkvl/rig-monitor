from pysnmp.entity.rfc3413.oneliner import cmdgen

def get_oid(host, community, oid):
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((host, 161)),
        oid
    )
    res = None
    for vb in varBinds:
        res = vb[1]
        break
    return res

def __get_oid(host, community, oid):
    return "{}.{}: {}".format(host, community, oid)

class NetworkTrafficStats(object):

    def __init__(self, conf):
        self.conf = conf

    def query(self):
        result = {}
        for h in self.conf:
            result[h] = {}
            for intf in self.conf[h]['query']:
                result[h][intf] = {}
                for k in self.conf[h]['query'][intf]:
                    result[h][intf][k] = None
                    result[h][intf][k] = int(globals()["__get_oid"](self.conf[h]['host'],
                                                                self.conf[h]['community'],
                                                                self.conf[h]['query'][intf][k])) * 8
        return result
