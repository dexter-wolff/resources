from Utility import Input

from Utility import WebScraping

web = WebScraping.WebScraper("https://aryanshakya.github.io/")

test = Input.speak(web)

# test = Input.speak("now this is tough to say")

# test2 = Input.speak("""सभी मनुष्यों को गौरव और अधिकारों के मामले में जन्मजात स्वतन्त्रता और समानता प्राप्त है। उन्हें बुद्धि और अन्तरात्मा की देन प्राप्त है और परस्पर उन्हें भाईचारे के भाव से बर्ताव करना चाहिये।""")