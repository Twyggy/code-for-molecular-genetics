import re

AS = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': ['Met', 'start'],
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'stopp', 'UAG': 'stopp',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'stopp', 'UGG': 'Trp',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}


def translate_mRNA(mRNA):
    mRNA = mRNA.upper() #makes mRNA input in capital letters 
    splited = re.findall(r'\w{3}|\w+$', mRNA.upper()) #splits mRNA input into items with the length three letters
    output = []
    
    for i in range(len(splited)):
        last_stopp_index = 0
        last_start_index = 0

        def translator(words):
            if splited[i] in AS:
                return [AS[word] for word in words.split()] #translating mRNA into AS sequenses
            else:
                return 'Not found'

        objected = translator(splited[i]) #using translate() to transalte the mRNA to AS 
        stringified = objected[0]
        if 'stopp' in output:
            last_stopp_index = len(output) - output[::-1].index('stopp') #Dedicates the last start
        if 'start' in output:
            last_start_index = len(output) - output[::-1].index('start') #Dedicates the last stopp


# checks whether AUG should be translated to start or Met
        if splited[i] == 'AUG': 
            if last_start_index <= last_stopp_index:
                stringified = AS['AUG'][1]
            elif last_stopp_index > last_start_index:
                stringified = AS['AUG'][1]
            elif last_stopp_index < last_start_index:
                stringified = AS['AUG'][0]

#filters for items between start and stopp
        if last_start_index > last_stopp_index or splited[i] == 'AUG':
            output.append(stringified)
            if stringified == 'stopp':
                output.append(' ') # adds a space after stop

    start_indices = [i for i, x in enumerate(output) if x == 'start']
    stop_indices = [i for i, x in enumerate(output) if x == 'stopp']

    result = []

#filters what is between start and stop
    for start, stop in zip(start_indices, stop_indices):
        if start < stop:
            result.append(output[start+1:stop]) #filters everything between start and stop bei index

    result_strings = [' - '.join(sublist) for sublist in result] #connects items in array with hyphen ('-')
    
    #connects all inner arrays in to a string 
    result_combined = ''' 
'''.join(result_strings)
    
    return result_combined #returns a string with translated AS sequence