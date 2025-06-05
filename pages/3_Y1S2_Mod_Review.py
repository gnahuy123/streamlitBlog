import streamlit as st
from sidebar import render_sidebar

st.set_page_config(page_title="Y1S2", page_icon=":tada:", layout="wide")

render_sidebar()

st.title("Y1S2 Mod Review")

st.subheader("Context", divider=True)

st.write("I decided to overload heavily this semester as I had some SUs to spare. This led to me taking 32 MCs.")

st.markdown(" - **CS2030S**: Programming Methodology II")
st.markdown(" - **CS2040S**: Data Structures and Algorithms")
st.markdown(" - **MA1521**: Calculus for Computing")
st.markdown(" - **IS1108**: Digital Ethics and Data Privacy")
st.markdown(" - **ES2660**: Communicating in the Information Age")
st.markdown(" - **CDE2501**: Sustainable Cities")
st.markdown(" - **EG1311**: Design and Make")
st.markdown(" - **MUA1192**: Chamber Singers")
st.markdown(" - **CFG1003**: Financial Wellbeing – Introduction")
st.markdown(" - **CFG1004**: Financial Wellbeing – Art and Science of Investing")


st.subheader("CS2030S Programming Methodology II", divider=True)
st.image('pictures/CS2030s-passTestcase.jpg', 'Figure 1. Happy Me after finishing exercise3')
st.write("Builds on CS1101S, introducing more advanced Object-Oriented and Functional Programming concepts. I got an A.")

st.write("""
**Workload: 9/10**  
2 hours of (dry) lectures each week, followed by a quiz and a lab assignment that typically took me 1–2 days to complete. 
The labs had multiple parts and required passing all test cases while maintaining clean and efficient code structure.
I often spent a lot of time—up to 12 hours—on a single assignment. Toward the later assignments, even after several days of effort, I sometimes couldn't complete them and had to resort to AI help.
On the bright side, the effort put into these assignments helped solidify my understanding, so by the time I revised for finals, I was already familiar with most of the concepts.
""")

st.write("""
**Enjoyability: 7/10**  
For most assignments, I would start off stuck, staring blankly at the screen. But eventually, I’d have a eureka moment that helped me break through and start coding. 
Solving the problems and passing all test cases was very satisfying. That said, some questions were overly difficult and frustrating, especially after hours of effort, which lowered my overall enjoyment.
""")

st.write("**What I did that worked/didn't work:**")
st.markdown("-  **Worked**: Diligently learned how to use VIM. During the first 2 weeks before tutorials started, I had more time and practiced using VIM, which helped me code faster during practicals.")
st.markdown("-  **Worked**: Tried my best not to use AI or copy code for assignments. This gave me more confidence for practicals and reinforced my understanding of OOP and functional programming.")
st.markdown("-  **Worked**: Initially tried watching the lectures, but they were quite dry. Eventually, I switched to reading the notes provided, which were very comprehensive and allowed me to go at my own pace.")

st.subheader("CS2040S Data Structures and Algorithms", divider=True)

st.write("The infamous Data Structures and Algorithms module. I got an A-.")


st.write("""
**Story Time**  
I entered this module feeling confident, as I had done a lot of LeetCode prep before university. From LeetCode, I learned to recognize patterns and apply certain data structures to solve problems.
However, CS2040S emphasized theoretical proofs—proving algorithm correctness and time complexity—rather than just application.
The midterm format was also different from past years, which threw me off. I ended up scoring below the 25th percentile for the midterms.

But I locked in after that. I began focusing on understanding the *why* behind the proofs, not just the *how*. I spent more time practicing writing out algorithms and explaining them clearly, 
which helped in conveying my thoughts during exams. Consultations with Eldrick also helped me gain clarity and confidence. I estimate I scored around the top 10% for the finals (assuming a normal distribution).
""")

st.image('pictures/CS2040s-perf.jpg', 'Figure 2. CS2040S grades')

st.write("""
**Workload: 8/10**  
3 hours of lectures per week, 1-hour recitation, and a 2-hour tutorial. Recitations and tutorials required preparing answers for worksheet questions in advance. 
There were also programming assignments that took me about 3 hours on average. I spent about double the lecture time reviewing proofs and internalizing concepts.
""")

st.write("""
**Enjoyability: 8/10**  
Intellectually challenging and stimulating. Lectures were heavy on proof techniques and theoretical understanding. Tutorials and recitations showed elegant problem-solving tricks. 
The programming assignments provided useful hands-on experience and solidified the abstract concepts.
""")

st.write("**What I did that worked/didn't work:**")

st.markdown("-  **Worked**: Focused on understanding the underlying theory and asking *why* each concept or proof works, instead of just memorizing how to solve problems.")
st.markdown("-  **Didn’t work**: Initially over-relied on prior LeetCode knowledge and underestimated the theoretical depth required, which caused me to struggle during midterms.")

st.subheader("MA1521 Calculus for Computing", divider=True)

st.write("Introductory calculus module meant for computing students. I got a B+")

st.write(
    "To be honest, I wasn’t very invested in this module. I only started studying one day before the exam and rushed through the examples to prep. "
    "First 5 chapters were roughly taught in H2 maths and I therefore banked on that knowledge to pass and then SU"
    "I didn’t attend lectures or tutorials, which definitely hurt my understanding. In the final exam, I only managed to attempt 3 out of 10 questions."
)

st.write(
    "While I’m generally quite interested in math mods, I found it hard to enjoy this one because it relied heavily on computation and offered barely any mathematical intuition. "
    "The lectures were dry and uninspiring, and by Week 3, I had pretty much given up on trying to keep up with the content."
)

st.write("**Workload: 0.5/10**")
st.write(
    "From a pure time-commitment perspective, the workload could be low if you’re not engaging with the content much — like I did. "
    "There were lectures and tutorials, but since I skipped most of them, my weekly time spent was basically zero until the final week."
)

st.write("**Enjoyability: 1/10**")
st.write(
    "I found it hard to stay interested because the teaching style didn’t click with me. If the professor had been more engaging or enthusiastic, I might have given the module a proper try. "
    "Friends of mine who later took MA2001 (which is used in DSA) mentioned that it was more rigorous and focused on proofs, which made it more enjoyable than the largely computational approach here."
)

st.write("**What I did that worked/didn’t work**")
st.markdown("-  **Didn’t Work**  \n Only started studying the day before the final and skipped most of the semester’s learning — obviously not ideal. Definitely wouldn’t recommend this approach.")
st.markdown("-  **Didn’t Work**  \n Not going for tutorials meant I didn’t have the chance to clarify doubts or build a consistent understanding. I paid the price in the exam.")




