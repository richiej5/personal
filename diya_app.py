import streamlit as st

st.title("To the one and only, Diya 💫")

# Question 1: Are you happy?
happy = st.radio("Are you happy?", options=["", "yes", "no"], index=0, key="happy")

if happy == "yes":
    # Question 2: Excited for birthday?
    excited = st.radio("Are you excited for your birthday?", options=["", "yes", "no"], index=0, key="excited")
    
    if excited == "yes":
        # Question 3: Best friend?
        bestfriend = st.radio("Do you consider myself as your best friend?", options=["", "yes", "no"], index=0, key="bestfriend")
        
        if bestfriend == "yes":
            # Question 4: Promise to stay?
            promise = st.radio("Promise to stay forever?", options=["", "yes", "no"], index=0, key="promise")
            
            if promise == "yes":
                st.success("Happy birthdayyyyyyyyyyyyy prettyyyyyy girl, ❤❤you have no idea what you mean to me, the closest i have ever been to somebody, the only person to know me in and out. Every second spent with you feels so nice and soothing, we laugh, we support each other, we fight, sometimes you slap too but its fine as i know its always my fault. Sometimes i feel mera kya hi hota if you had not sent me that screenshot, meri life itni boring ho jaati na. I dont care what you think of yourself or what made you think things like these, all i know is you are pretty, you're cute, you are perfect, you are always the active one between us, you are sweet. No matter what you say or people say ik you, i promise to never drift away from you or to judge you for your acts in the past or future. All you need to know is that its never your fault, you have zero flaws, you look perfect and beautiful the way you are. You have always made me so comfortable and loved that it didnt take me much time to share literally every single thing of my life with you. ik i might not be that smart enough to understand things as you want or that expressive but i promise to never knowningly hurt you and try not to do it unknowingly too. Thank you for always being there. Thank you for changing me so drastically that you yourself ended up falling for it🫠.I'll not ask you to promise to stay forever because you have already agreed to that that's why you are reading this. Just your presence is enough to make my day. I love you😘")
            elif promise == "no":
                st.warning("Please say yes! I really hope you mean it 💫")

        elif bestfriend == "no":
            st.warning("I'll ask that again... take your time to think 💭")
    
    elif excited == "no":
        st.warning("I'll ask you again... I know the excitement is there!")

elif happy == "no":
    st.warning("Let's try that again...")

