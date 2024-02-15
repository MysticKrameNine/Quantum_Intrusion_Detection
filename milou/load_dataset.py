from pandas import DataFrame
import csv

pts = ['tcp','udp','icmp']

services = ['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime',
            'discard', 'domain', 'domain_u', 'echo', 'eco_i', 'ecr_i', 'efs',
            'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest',
            'hostnames', 'http', 'http_2784', 'http_443', 'http_8001',
            'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell', 'ldap', 'link',
            'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns',
            'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other',
            'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i',
            'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh', 'sunrpc',
            'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time', 'urh_i',
            'urp_i', 'uucp', 'uucp_path', 'vmnet', 'whois', 'X11', 'Z39_50']

flags = ['OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3',
         'SF', 'SH']

pt_dict = {}
service_dict = {}
flag_dict = {}
list_dict_map = [{'list':pts,'dict':pt_dict},
                 {'list':services,'dict':service_dict},
                 {'list':flags,'dict':flag_dict}]

for e in list_dict_map:
    l=e['list']
    d=e['dict']
    n = len(l)
    for i in range(n):
        att = l[i]
        d[att] = i/n

def encode_class(c):
    return float(c!='normal')

def encode_protocol_type(pt):
    return pt_dict[pt]

def encode_service(s):
    return service_dict[s]

def encode_flag(f):
    return flag_dict[f]/10

atts = [('duration',float),
        ('protocol_type',encode_protocol_type),
        ('service',encode_service),
        ('flag',encode_flag),
        ('src_bytes',float),
        ('dst_bytes',float),
        ('land',float),
        ('wrong_fragment',float),
        ('urgent',float),
        ('hot',float),
        ('num_failed_logins',float),
        ('logged_in',float),
        ('num_compromised',float),
        ('root_shell',float),
        ('su_attempted',float),
        ('num_root',float),
        ('num_file_creations',float),
        ('num_shells',float),
        ('num_access_files',float),
        ('num_outbound_cmds',float),
        ('is_host_login',float),
        ('is_guest_login',float),
        ('count',float),
        ('srv_count',float),
        ('serror_rate',float),
        ('srv_serror_rate',float),
        ('rerror_rate',float),
        ('srv_rerror_rate',float),
        ('same_srv_rate',float),
        ('diff_srv_rate',float),
        ('srv_diff_host_rate',float),
        ('dst_host_count',float),
        ('dst_host_srv_count',float),
        ('dst_host_same_srv_rate',float),
        ('dst_host_diff_srv_rate',float),
        ('dst_host_same_src_port_rate',float),
        ('dst_host_srv_diff_host_rate',float),
        ('dst_host_serror_rate',float),
        ('dst_host_srv_serror_rate',float),
        ('dst_host_rerror_rate',float),
        ('dst_host_srv_rerror_rate',float),
        ('class',encode_class),
        ('difficulty_level',float)]

feature_names = [a[0] for a in atts]

def load_dataset(filename):
    n=len(atts)
    csvf=open(filename)
    data = [[atts[i][1](r[i]) for i in range(n)] for r in csv.reader(csvf)]
    df = DataFrame(data,columns=feature_names)
    df = df.drop(columns=['difficulty_level'])
    return df.drop(columns=['class']),df['class']

X_train,y_train = load_dataset('../data/nsl-kdd/KDDTrain+.txt')
X_test,y_test = load_dataset('../data/nsl-kdd/KDDTest+.txt')

# dereference the attributes we are not using
feature_names = feature_names[:-2]

print(X_train.dtypes)
print(X_train.shape)
