import streamlit as st

st.set_page_config(page_title="Preparation for CS", page_icon=":tada:", layout="wide")

st.title("How to Prepare for CS in University")

st.subheader("Preface")

st.write("""
I completed my Junior College education in 2021 and enlisted in the Singapore Armed Forces for National Service. While some of my peers revised or taught tuition to stay mentally active, I found the rigours of being a soldier left me with little energy or motivation to continue my studies. 

Fearing I would fall behind in this notoriously tough course, I began preparing in November 2023, about 8 months before matriculation.
""")

st.markdown("- I come from a Junior College background (Subject combination: PCMe – AAA/C)")
st.markdown("- My favourite subject in JC was H2 Maths")
st.markdown("- I had no formal coding experience")
st.markdown("- I started coding only 1 year before matriculation")

st.subheader("CS50 Harvard", divider=True)

st.image("pictures/CS50.jpg", caption="Figure 1: Prof. David Malan and his famous course CS50")

st.write("""
CS50 is a free, entry-level Computer Science course taught by Harvard professors. It introduces fundamental concepts and practical programming skills. 

There are various versions available, but I recommend **CS50x** for Computer Science students as it focuses more on the core foundations you'll need.
""")

st.subheader("Pros")

st.markdown("- Gives you a good overview of what Computer Science is (great if you’re unsure if CS is for you)")
st.markdown("- Familiarizes you with programming syntax (in NUS, this is often covered in just one lecture!)")
st.markdown("- Covers fundamental concepts that overlap with NUS's CS1101S")

st.subheader("Cons")

st.markdown("- You could instead read the [CS1101S textbook](https://sourceacademy.org/sicpjs/) for more relevant material")
st.markdown("- Steep learning curve (see my personal experience below)")
st.markdown("- It's self-directed, so getting personalised help can be challenging")

st.write("""
The learning curve was extremely steep for me. After months of NS, I experienced a sort of “brain rot,” and since coding was unlike anything I'd done before, it took a lot to grasp the basics. 

In fact, understanding these foundational concepts has been the **hardest** part of my CS journey so far.
""")

st.write("""Why was CS50 so hard for me? Let's compare it with a H2 Math question.""")

st.code("""
Find the maximum point of f(x) = x^2 + 2x + 1

From what I remember, we just needed to follow the steps:
 - Differentiate f(x)
 - Solve f'(x) = 0
 - Use the first or second derivative test to check if it's a max/min
""")

st.write("""
As you can see, Math problems often follow a set of procedures. You just need to memorise and apply them to similar questions.

Now compare this to a CS50 question:
""")

st.code("""
Create a function that takes an integer and prints a pyramid like this:
For n = 4

   #  #
  ##  ##
 ###  ###
####  ####
""")

st.write("""
In lectures, the professor only taught C syntax like loops and conditionals. I was completely lost when I saw this problem.

The key difference: CS problems don’t just test your content knowledge — they require **problem-solving**. There’s no spoon-feeding. You must break down the problem and figure it out step by step.
""")

st.write("""
Through these two examples, I hope you see how Computer Science differs drastically from what we’re used to — both in **content** and in the **way we think**.

Since I struggled with CS50x initially, I pivoted to **CS50p** (Python version) before returning to CS50x. It helped build my confidence and gave me a real advantage in future NUS courses.
""")

st.subheader("LeetCode", divider=True)

st.write("""
LeetCode builds on your understanding of Data Structures and Algorithms, and further sharpens your problem-solving skills.

During CS50, I discovered that I enjoyed solving algorithmic challenges — they forced me to think critically and creatively.

So I spent the rest of my holidays grinding LeetCode, starting with the NeetCode roadmap.
""")

st.subheader("Pros")

st.markdown("- Sharpens problem-solving skills")
st.markdown("- Highly applicable to CS2040S")
st.markdown("- Helps you learn to **design** solutions, not just apply them")
st.markdown("- Crucial for technical interviews — it's never too early to start")
st.markdown("- (Most importantly) I enjoyed it")

st.subheader("Cons")

st.markdown("- Can be frustrating at times — takes a while to get the hang of")
st.markdown("- Requires focus, patience, and persistence")
st.markdown("- Not project-based, so it doesn't directly add to your portfolio")

st.write("""
I highly recommend the NeetCode roadmap (see below) because it offers a structured path — starting with beginner-friendly problems and gradually introducing more advanced ones. 

It helps build your programming intuition, which takes time to develop but lasts a lifetime.
""")

st.image("pictures/neetcode.png", caption="Figure 2: NeetCode roadmap — structured practice for DSA")

st.subheader("Takeaways")

st.write("""
I could have spent my time working on personal projects or pre-reading course content, but I chose this path because I **enjoyed** it.

If there’s one piece of advice I could give about preparing before matriculation, it’s this:

**Do what you enjoy.**

University will be stressful — especially during the transition — and you want to start your journey energized, not burned out.
""")










