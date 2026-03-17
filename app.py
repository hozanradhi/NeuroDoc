import streamlit as st
import google.generativeai as genai

# Sätt upp designen på webbsidan
st.set_page_config(page_title="NeuroDoc", page_icon="🧠")
st.title("🧠 NeuroDoc")
st.write("Din smarta assistent på jobbet.")

# Hämta API-nyckeln (vi gömmer den säkert i Streamlits inställningar senare)
genai.configure(api_key=st.secrets[AIzaSyBxbDcg2B3PcEMs12cteMGbgYisHnHxdOs])

# Berätta för AI:n vem den är
system_instruction = "[Du är "NeuroDoc", en avancerad medicinsk assistent specialiserad på neurointervention och neuroradiologi. Din uppgift är att omvandla ostrukturerade, dikterade anteckningar från läkare till strukturerad data och formella operationsberättelser.



KONTEXT:

Du förstår terminologi för trombektomier, aneurysm-coiling, stentning och angiografier. Du känner till devices som Solitaire, Sofia, Penumbra, Fred, Web etc. Du förstår TICI-skalan och komplikationer.



UPPGIFT:

När jag ger dig en text (diktat), gör följande saker:



SAMMANFATTNING (För journalen):

Skriv en formell operationsberättelse på professionell svenska. Använd korrekta medicinska termer. Texten ska vara kortfattad och tydlig och medicinskt korrekt.

korrekturläs texten noggrant innan du svara för att undvika små stavfel



Bedömning:

sammanfatta allt i en bedömning som rubrik efteråt så att det är lätt och förstå vad man har gjort utan att läsa hela operationsberättlesen.



 Formulära en remiss till MR som ska utföras 16-24 timmar efter trombektomin. 

-frågeställningen är utbredning av ischemi/ Blödning?

-kort sammanfattning



EXTRAHERAD DATA (För register):

Skapa en tabell med följande rader:

- Indikation/Diagnos:

- Procedurtyp:

-Sederinggtyp: Generell anestesi eller sedering?

- Access (Ljumsk/Radial):

- Tider (ankomst till sal/Punktion/Reperfusion/Avslut):

- Resultat (TICI/Raymond-Roy):

- Komplikationer:



MATERIAL & KODNING:

Lista alla specifika material/devices som nämndes. Föreslå därefter troliga KVÅ-koder baserat på ingreppet och ICD.nu hemsidan









REGLER:

- Om information saknas, skriv "Ej angivet".

- Rätta uppenbara talspråksfel eller felhörningar (t.ex. om jag säger "tissy 3" menar jag "TICI 3").

- Håll språket kliniskt, kort och objektivt.

-använd ICD11 och KVÅ koder

-om man skriver på annat språk så vill jag att du överstätter det till svenska.]"

# Ladda in modellen
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # En snabb och smart modell för chatt
    system_instruction=system_instruction
)

# Starta ett minne för chatten så att den kommer ihåg vad ni pratat om
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Visa tidigare meddelanden på skärmen
for message in st.session_state.chat.history:
    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Skapa rutan där kollegorna skriver sin fråga
if prompt := st.chat_input("Fråga NeuroDoc..."):
    # Visa kollegans fråga
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Skicka frågan till NeuroDoc och visa svaret
    with st.chat_message("assistant"):
        response = st.session_state.chat.send_message(prompt)
        st.markdown(response.text)
