calls = 0
def count_calls():
    global calls
    calls = calls +1
def string_info(string):
    print(tuple([len(string), string.upper(), string.lower()]))
    count_calls()
def is_contains(string, list_to_search):
    string = 'Urban'
    list_to_search = ['z', 'Urban', 'z']
    string_new = string.lower() 
    list_to_search_new = [s.lower() for s in list_to_search]
    if string_new in list_to_search_new:
        print (True)
    else:
        print (False)
        count_calls()
string_info('Hello')
string_info('Universe')
is_contains('LuCK', ['SUN', 'fun', 'luck'])
print(calls)