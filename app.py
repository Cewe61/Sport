import streamlit as st
from pathlib import Path
import time

st.set_page_config(
    page_title="Gymnastik – Mittwoch & Sonntag",
    page_icon="🏋️",
    layout="centered"
)

# --------------------------------------------------
# Hilfsfunktionen
# --------------------------------------------------

def bild_anzeigen(pfad, icon="🏃"):
    if Path(pfad).exists():
        st.image(pfad, use_container_width=True)
    else:
        st.markdown(
            f"<div style='font-size:70px;text-align:center'>{icon}</div>",
            unsafe_allow_html=True
        )

def timer_widget(key, sekunden, titel="Timer"):
    platzhalter = st.empty()

    if st.button(f"⏱️ {titel} starten", key=f"start_{key}"):
        for rest in range(sekunden, 0, -1):
            minuten = rest // 60
            sek = rest % 60
            platzhalter.info(f"{titel}: {minuten:02d}:{sek:02d}")
            time.sleep(1)
        platzhalter.success("✅ Fertig")
    else:
        minuten = sekunden // 60
        sek = sekunden % 60
        platzhalter.info(f"{titel}: {minuten:02d}:{sek:02d}")

# --------------------------------------------------
# ÜBUNGEN
# --------------------------------------------------

uebungen = [
    {
        "name": "Liegestütz",
        "ziel": "Brust, Schulter, Trizeps, Rumpf",
        "umfang": "8–15 Wiederholungen",
        "ausfuehrung":
            "Hände schulterbreit aufsetzen. Körper von Kopf bis Ferse in einer Linie halten. "
            "Kontrolliert absenken und wieder hochdrücken.",
        "bild": "bilder/liegestuetz.png",
        "icon": "💪",
        "timer": None
    },
    {
        "name": "Bird Dog",
        "ziel": "Rumpfstabilität, Rücken, Gesäß",
        "umfang": "8–10 je Seite",
        "ausfuehrung":
            "Im Vierfüßlerstand einen Arm nach vorne und das gegenüberliegende Bein nach hinten strecken. "
            "Becken stabil halten. Dann Seite wechseln.",
        "bild": "bilder/bird_dog.png",
        "icon": "🐕",
        "timer": None
    },
    {
        "name": "Kniebeuge",
        "ziel": "Oberschenkel, Gesäß, Rumpf",
        "umfang": "12–15 Wiederholungen",
        "ausfuehrung":
            "Füße schulterbreit. Gesäß nach hinten und unten führen. "
            "Knie in Richtung der Fußspitzen halten. Kontrolliert wieder aufrichten.",
        "bild": "bilder/kniebeuge.png",
        "icon": "🦵",
        "timer": None
    },
    {
        "name": "Side Plank",
        "ziel": "Seitliche Bauchmuskulatur, Rumpfstabilität",
        "umfang": "30 Sekunden je Seite",
        "ausfuehrung":
            "Seitlich auf dem Unterarm abstützen. Becken anheben, "
            "bis Schulter, Hüfte und Fuß möglichst eine Linie bilden. Danach Seite wechseln.",
        "bild": "bilder/side_plank.png",
        "icon": "↔️",
        "timer": 30
    },
    {
        "name": "Glute Bridge",
        "ziel": "Gesäß, hintere Oberschenkel, Rücken",
        "umfang": "12–15 Wiederholungen",
        "ausfuehrung":
            "Rückenlage, Knie gebeugt. Becken durch Anspannen des Gesäßes anheben. "
            "Oben kurz halten und langsam wieder absenken.",
        "bild": "bilder/glute_bridge.png",
        "icon": "🌉",
        "timer": None
    },
    {
        "name": "Plank",
        "ziel": "Bauch und gesamte Rumpfmuskulatur",
        "umfang": "45 Sekunden",
        "ausfuehrung":
            "Auf Unterarmen und Fußspitzen abstützen. Bauch aktiv anspannen. "
            "Kopf, Rücken und Beine möglichst in einer geraden Linie halten.",
        "bild": "bilder/plank.png",
        "icon": "▬",
        "timer": 45
    },
    {
        "name": "Back Step",
        "ziel": "Beine, Gesäß, Gleichgewicht",
        "umfang": "8–10 je Seite",
        "ausfuehrung":
            "Aus dem Stand einen kontrollierten Schritt nach hinten machen. "
            "Beide Knie beugen und dann wieder in den Stand zurückkehren.",
        "bild": "bilder/back_step.png",
        "icon": "🔙",
        "timer": None
    },
]

# --------------------------------------------------
# DEHNUNGEN
# --------------------------------------------------

dehnungen = [
    {
        "name": "Hüftbeuger",
        "dauer": "40 Sekunden je Seite",
        "timer": 40,
        "bild": "bilder/dehnung_hueftbeuger.png",
        "icon": "🧘",
        "text":
            "Halbkniestand. Becken leicht nach vorne schieben, ohne ins Hohlkreuz zu gehen. "
            "Dehnung vorne an Hüfte und Oberschenkel spüren."
    },
    {
        "name": "Oberschenkelrückseite",
        "dauer": "40 Sekunden je Seite",
        "timer": 40,
        "bild": "bilder/dehnung_oberschenkelrueckseite.png",
        "icon": "🧘",
        "text":
            "Ein Bein nach vorne ausstrecken. Rücken möglichst gerade halten und "
            "Oberkörper langsam nach vorne neigen."
    },
    {
        "name": "Gesäß",
        "dauer": "40 Sekunden je Seite",
        "timer": 40,
        "bild": "bilder/dehnung_gesaess.png",
        "icon": "🧘",
        "text":
            "In Rückenlage einen Fuß auf das gegenüberliegende Knie legen und "
            "das andere Bein langsam zum Körper ziehen."
    },
    {
        "name": "Brust & Schulter",
        "dauer": "40 Sekunden je Seite",
        "timer": 40,
        "bild": "bilder/dehnung_brust_schulter.png",
        "icon": "🧘",
        "text":
            "Arm seitlich an Wand oder Türrahmen anlegen und Oberkörper kontrolliert davon wegdrehen."
    },
    {
        "name": "Rücken",
        "dauer": "45 Sekunden",
        "timer": 45,
        "bild": "bilder/dehnung_ruecken.png",
        "icon": "🧘",
        "text":
            "Aus dem Vierfüßlerstand das Gesäß Richtung Fersen führen und die Arme weit nach vorne strecken."
    },
    {
        "name": "Pezziball",
        "dauer": "45 Sekunden",
        "timer": 45,
        "bild": "bilder/dehnung_pezziball.png",
        "icon": "⚪",
        "text":
            "Hockend vor dem Pezziball positionieren und den Rücken auf den Pezziball legen. "
            "Brustkorb öffnen, ruhig weiteratmen und die Dehnung angenehm halten."
    },
]

# --------------------------------------------------
# STATUS
# --------------------------------------------------

if "seite" not in st.session_state:
    st.session_state.seite = "start"

if "runde" not in st.session_state:
    st.session_state.runde = 1

if "uebung" not in st.session_state:
    st.session_state.uebung = 0

# --------------------------------------------------
# STARTSEITE
# --------------------------------------------------

if st.session_state.seite == "start":

    st.title("🏋️ Mein Zirkeltraining")
    st.subheader("Mittwoch & Sonntag")

    st.info(
        "3 Runden • 7 Übungen\n\n"
        "Im Anschluss kann die Dehnung separat gestartet werden."
    )

    st.markdown("### Trainingsablauf")
    for nummer, u in enumerate(uebungen, 1):
        st.write(f"**{nummer}. {u['name']}** – {u['umfang']}")

    st.markdown("---")

    if st.button("▶️ Zirkeltraining starten", type="primary", use_container_width=True):
        st.session_state.runde = 1
        st.session_state.uebung = 0
        st.session_state.seite = "zirkel"
        st.rerun()

    if st.button("🧘 Dehnung", use_container_width=True):
        st.session_state.seite = "dehnung"
        st.rerun()

# --------------------------------------------------
# ZIRKEL
# --------------------------------------------------

elif st.session_state.seite == "zirkel":

    runde = st.session_state.runde
    nr = st.session_state.uebung
    u = uebungen[nr]

    st.title(f"Runde {runde} von 3")

    fortschritt = ((runde - 1) * len(uebungen) + nr) / (3 * len(uebungen))
    st.progress(fortschritt)

    st.header(f"{u['icon']} {u['name']}")
    bild_anzeigen(u["bild"], u["icon"])

    st.markdown(f"### {u['umfang']}")
    st.write(f"**Trainiert:** {u['ziel']}")
    st.info(u["ausfuehrung"])

    if u["timer"] is not None:
        if u["name"] == "Side Plank":
            st.caption("Den Timer bitte je Seite einmal starten.")
        timer_widget(
            key=f"zirkel_{runde}_{nr}",
            sekunden=u["timer"],
            titel=u["name"]
        )

    st.markdown("---")

    if st.button("✅ Fertig – nächste Übung", type="primary", use_container_width=True):

        if nr < len(uebungen) - 1:
            st.session_state.uebung += 1
        elif runde < 3:
            st.session_state.runde += 1
            st.session_state.uebung = 0
        else:
            st.session_state.seite = "zirkel_fertig"

        st.rerun()

    if st.button("⌂ Training beenden"):
        st.session_state.seite = "start"
        st.rerun()

# --------------------------------------------------
# ZIRKEL FERTIG
# --------------------------------------------------

elif st.session_state.seite == "zirkel_fertig":

    st.title("✅ Zirkel geschafft")
    st.success("3 Runden vollständig absolviert.")

    if st.button("🧘 Dehnung starten", type="primary", use_container_width=True):
        st.session_state.seite = "dehnung"
        st.rerun()

    if st.button("⌂ Zur Startseite", use_container_width=True):
        st.session_state.seite = "start"
        st.rerun()

# --------------------------------------------------
# DEHNUNG
# --------------------------------------------------

elif st.session_state.seite == "dehnung":

    st.title("🧘 Dehnung")

    st.write(
        "Die Dehnung ist bewusst ein eigener Programmteil und kann jederzeit separat gestartet werden."
    )

    for nr, d in enumerate(dehnungen, 1):
        with st.expander(f"{nr}. {d['name']} – {d['dauer']}", expanded=False):
            bild_anzeigen(d["bild"], d["icon"])
            st.write(d["text"])
            timer_widget(
                key=f"dehnung_{nr}",
                sekunden=d["timer"],
                titel=d["name"]
            )

    st.markdown("---")

    if st.button("✅ Dehnung beendet", type="primary", use_container_width=True):
        st.session_state.seite = "start"
        st.rerun()
