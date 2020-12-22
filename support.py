def parse_csv(f):
    is_text_entry = True
    csv_list = []
    for line in f:
        entry_list = []
        temporary_string = ''
        for symbol in line:
            if (symbol in ',\n') and is_text_entry:
                entry_list.append(temporary_string)
                temporary_string = ''
            elif symbol == '"':
                is_text_entry = not is_text_entry
            else:
                temporary_string += symbol
        csv_list.append(entry_list)
    csv_list.remove(csv_list[0])
    return csv_list