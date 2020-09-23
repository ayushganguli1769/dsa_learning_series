from functools import cmp_to_key
def cmp_chef(chef_a,chef_b):
    global chef_dict
    if chef_dict[chef_a]['count'] < chef_dict[chef_b]['count']:
        return -1 
    elif chef_dict[chef_a]['count'] > chef_dict[chef_b]['count']:
        return 1
    else:
        if chef_a < chef_b:
            return 1
        else:
            return -1
def cmp_country(country_a,country_b):
    global country_dict
    if country_dict[country_a] < country_dict[country_b]:
        return -1
    elif country_dict[country_a] > country_dict[country_b]:
        return 1
    else:
        if country_a < country_b:
            return 1
        else:
            return -1
(n,m) = map(int,input().strip().split())
chef_dict = {}
country_dict = {}
chef_dict = {}
for _ in range(n):
    (chef_name,country_name) = map(str,input().strip().split())
    chef_dict[chef_name] = {'country':country_name,'count':0}
    country_dict[country_name] = 0
for _ in range(m):
    chef_name = str(input())
    chef_dict[chef_name]['count'] += 1
    country_dict[chef_dict[chef_name]['country']] += 1
chef_list = list(chef_dict.keys())
country_list = list(country_dict.keys())
chef_list = sorted(chef_list,key=cmp_to_key(cmp_chef))
country_list = sorted(country_list,key=cmp_to_key(cmp_country))
print(country_list[len(country_list)-1])
print(chef_list[len(chef_list)-1])