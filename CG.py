def count_cg_percent(dna_sequence):
#return GC content in percent, 
    if not dna_sequence:
        return 0
    seq = dna_sequence.upper()
    g_count = seq.count('G')
    c_count = seq.count('C')
    return (g_count + c_count) / len(seq) * 100

def show_max_min_gc(sequences):
#return MAX and MIN 
    if not sequences:
        print('NULL')
        return
    gc_values = [count_cg_percent(seq) for seq in sequences]
    print(f'MAX GC: {max(gc_values):.6f}%')
    print(f'MIN GC: {min(gc_values):.6f}%')

def show_all_gc(sequences):
#show all sequences with GC content in percent
    if not sequences:
        print('NULL')
        return
    print('\n--- ALL GC VALUES ---')
    for i, seq in enumerate(sequences):
        gc = count_cg_percent(seq)
        print(f'Sequence {i+1}: {gc:.6f}%')


def data_fasta_parsing(fileNameData):
    sequenceList = []
    currentSequence = '' 

    with open(fileNameData, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if currentSequence:
                    sequenceList.append(currentSequence)
                    currentSequence = '' 
            else:
                currentSequence += line
                
        if currentSequence:
            sequenceList.append(currentSequence)
            
    return sequenceList

while 1:
    print('\n--- MENU ---')
    print('1. Analyze DNA')
    print('2. EXIT')

    main_choice = input('Select an action: ')
    
    if main_choice == '1':
        filename = input('Enter the FASTA file name: ')
        try:
            sequence_list = data_fasta_parsing(filename)

            print('\nSelect analysis mode:')
            print('1. Show MAX and MIN GC')
            print('2. Show ALL GC values')

            sub_choice = input('Your choice: ') 
            
            if sub_choice == '1':
                show_max_min_gc(sequence_list)
            elif sub_choice == '2':
                show_all_gc(sequence_list) 
            else:
                print('Incorrect input')
            
        except FileNotFoundError:
            print('File not found')

    elif main_choice == '2':
        print('Goodbye')
        break
    else:
        print('Incorrect input')
