f = open(r"..\Lab_2\steam.csv", encoding='utf-8')
import dialogue
import support

counter_i = 0
counter_j = 0
text_for_person = support.parse_csv(f)
f.close()

dialogue.dialogue_table(text_for_person)
