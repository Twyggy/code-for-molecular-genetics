import re 

AS = {
    'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': ['Met','start'],
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

while True:
    # mRNA = 'AUGGAGCCUCUGAAGGCCUGUGCUCAAGGGAGAAGUUGGAGGUGUGAAGAGCUGGGCAGUGUGAGGUGGUGGAAGAGCUGUGAGGCAGCAGUCUGAGGAGGUCUGUCCUCCUGGUGAUGUGGAGUAGCAGGAGGAAGAUGAGGUGGUGGUGGUGGUGGAAGAUGGUGGUGGAAGAGGAUGUGGAAGAUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGAUGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGAUGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUG'
    # mRNA = 'UGG AUG GGA CUA ACA UAA CUA UGG AUG GGA CUA ACA UAA CUA'
    mRNA = input('Enter mRNA sequence: ')
    mRNA = mRNA.upper()
    # 'AUGGAGCCUCUGAAGGCCUGUGCUCAAGGGAGAAGUUGGAGGUGUGAAGAGCUGGGCAGUGUGAGGUGGUGGAAGAGCUGUGAGGCAGCAGUCUGAGGAGGUCUGUCCUCCUGGUGAUGUGGAGUAGCAGGAGGAAGAUGAGGUGGUGGUGGUGGUGGAAGAUGGUGGUGGAAGAGGAUGUGGAAGAUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGAUGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGAUGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGUGGAAGGAGGUGGUGGUGGUGGUGGUGGUGGUG'
    # UGG AUG GGA CUA ACA UAA CUA UGG AUG GGA CUA ACA UAA CUA
    # mRNA = mRNA.upper()
    # splited = re.findall(r'\w{3}|\w+$', mRNA.upper())
    output = []
    lenght = 800

    def translate():
        splited = re.findall(r'\w{3}|\w+$', mRNA.upper())
        for i in range(len(splited)):
            last_stopp_index = 0
            last_start_index = 0
            
            def translator(words):
                if splited[i] in AS:
                    return [AS[word] for word in words.split()]
                else:
                    return'Not found'

            # output.append(translator(splited[i]))
            # Suche nach aufeinanderfolgenden dreibuchstabigen Wörtern, gefolgt von optionalen einzelnen oder mehreren Buchstaben am Ende
            # print(translator(splited[i]))
            objected = translator(splited[i])
            stringified = objected[0]
            if 'stopp' in output:
                last_stopp_index = len(output) - output[::-1].index('stopp') 
            if 'start' in output:
                last_start_index = len(output) - output[::-1].index('start')
            
            #print(last_start_index, last_stopp_index)

            if splited[i] == 'AUG':
                #print('catch')
                if last_start_index <= last_stopp_index:
                    stringified = AS['AUG'][1]
                elif last_stopp_index > last_start_index:
                    stringified = AS['AUG'][1]
                elif last_stopp_index < last_start_index:
                    stringified = AS['AUG'][0]
            
            # wenn man if-Schleife verwendet, werden nur alle sachen zweichen start und stopp gespoted…
            if last_start_index > last_stopp_index or splited[i] == 'AUG':
                output.append(stringified)
                if stringified == 'stopp':
                    output.append(' ')
                
        # print(output)
        
        allAS = ' '.join(output)
        # print('Alle Aminosäuren: ', allAS)
        
        # gibt den index von start und stopp
        start_indices = [i for i, x in enumerate(output) if x == 'start']
        stop_indices = [i for i, x in enumerate(output) if x == 'stopp']

        # print(start_indices, stop_indices)

        result = []

        # filtert, was zwischen start und stopp steht
        for start, stop in zip(start_indices, stop_indices):
            if start < stop:
                result.append(output[start+1:stop])

        # print(result)

        result_strings = [' - '.join(sublist) for sublist in result]
        result_combined = '''
    '''.join(result_strings)

        if result_combined == '':
            result_combined = "no AS sequence found ('-')"
        # print(result, 'test')
        print('AS sequence: ', result_combined)
        # outputstr = ' '.join(output) | wenn man stopp und start sehen möchte
        # outputstr = ' '.join(item for item in output if item not in ('start', 'stopp'))
        # print('Amino acid sequence:', outputstr)
        print(''' ''')
        
    translate()