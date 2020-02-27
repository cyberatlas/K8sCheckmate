def dictIterate(d, level):
    tabs = ''.join('\t' for i in range(0, level))
    for key, value in d.items():
        if isinstance(value, dict):
            # print("{0}{1}: ").format(tabs, key)
            print(f"{tabs}{key}: ")
            level += 1
            dictIterate(value, level)
        else:
            # print("{0}{1}: {2}".format(tabs, key, value))
            print(f"{tabs}{key}: {value}")

dictionary = {'cats': 'whiskers', 'dogs': { 'corgi': 'winston'}, 'KEY': 'walue', 'dict': { 'dict2': { 'special': 'times' }}, 'one': 'two'}

dictIterate(dictionary, 0)