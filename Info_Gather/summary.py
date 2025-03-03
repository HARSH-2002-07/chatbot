from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk

nltk.download('punkt_tab')

def summarize_text(text, num_sentences=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return " ".join([str(sentence) for sentence in summary])

text = """The president of the United States (POTUS) is the head of state and head of government of the United States. The president directs the executive branch of the federal government and is the commander-in-chief of the United States Armed Forces.
The power of the presidency has grown substantially since the first president, George Washington, took office in 1789. While presidential power has ebbed and flowed over time, the presidency has played an increasingly significant role in American political life since the beginning of the 20th century, carrying over into the 21st century with notable expansions during the presidencies of Franklin D. Roosevelt and George W. Bush. In modern times, the president is one of the world's most powerful political figures and the leader of the world's only remaining superpower. As the leader of the nation with the largest economy by nominal GDP, the president possesses significant domestic and international hard and soft power. For much of the 20th century, especially during the Cold War, the U.S. president was often called "the leader of the free world".
Article II of the Constitution establishes the executive branch of the federal government and vests executive power in the president. The power includes the execution and enforcement of federal law and the responsibility to appoint federal executive, diplomatic, regulatory, and judicial officers.  Based on constitutional provisions empowering the president to appoint and receive ambassadors and conclude treaties with foreign powers, and on subsequent laws enacted by Congress, the modern presidency has primary responsibility for conducting U.S. foreign policy. The role includes responsibility for directing the world's most expensive military, which has the second-largest nuclear arsenal.
The president also plays a leading role in federal legislation and domestic policymaking. As part of the system of separation of powers, Article I, Section 7 of the Constitution gives the president the power to sign or veto federal legislation. Since modern presidents are typically viewed as leaders of their political parties, major policymaking is significantly shaped by the outcome of presidential elections, with presidents taking an active role in promoting their policy priorities to members of Congress who are often electorally dependent on the president. In recent decades, presidents have also made increasing use of executive orders, agency regulations, and judicial appointments to shape domestic policy.
The president is elected indirectly through the Electoral College to a four-year term, along with the vice president. Under the Twenty-second Amendment, ratified in 1951, no person who has been elected to two presidential terms may be elected to a third. In addition, nine vice presidents have become president by virtue of a president's intra-term death or resignation. In all, 45 individuals have served 47 presidencies spanning 60 four-year terms. Donald Trump is the 47th and current president since January 20, 2025."""

summary = summarize_text(text, num_sentences=4)
print(summary)
