import random
from random import sample

class QuizGenerator:
    def __init__(self, data, topic_selected=None, q_number=None, word_searched=None):
        self.questions = data['domande']
        self.topics = data['tema']
        self.topic_selected = topic_selected
        self.q_number = q_number
        self.word_searched = word_searched

    def topic(self):

        if self.topic_selected == 'TUTTI':
            list_q_selected_topic = list(self.topics.keys())
        else:
            list_q_selected_topic = [k for k, v in self.topics.items() if self.topics[str(k)] == self.topic_selected]

        q_list = random.sample(list_q_selected_topic, k= self.q_number)

        return q_list

    def search(self):
        q_list = []
        list_q_selected_search = [k for k,v in self.questions.items() if str(self.word_searched) in str(v)]
        q_list = list_q_selected_search
        return q_list

    def exam(self):
        #
        q_list=[]
        scheda_esame = {'TEORIA DELLO SCAFO': 1, 'MOTORI': 1, 'SICUREZZA DELLA NAVIGAZIONE': 3,
                        'MANOVRA E CONDOTTA': 4, 'COLREG E SEGNALAMENTO MARITTIMO': 2, 'METEOROLOGIA': 2,
                        'NAVIGAZIONE CARTOGRAFICA ED ELETTRONICA': 4, 'NORMATIVA DIPORTISTICA E AMBIENTALE': 3}
        for topic in scheda_esame.keys():
            # creo una lista con tutti gli indici delle domande appartenenti al topic scelto
            q_topic_list = [k for k, v in self.topics.items() if self.topics[str(k)] == topic]
            q_temp_list = sample(q_topic_list, k=scheda_esame[topic])
            for q in q_temp_list:
                q_list.append(q)
        return q_list

    def error(self):
        # open file saved.json
        pass


