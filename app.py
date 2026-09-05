import streamlit as st
from pathlib import Path
from datetime import datetime

st.set_page_config(
    page_title="Gymnastik – Mittwoch & Sonntag",
    page_icon="🏋️",
    layout="centered"
)

# --------------------------------------------------
# Einstellungen
# --------------------------------------------------

TRAININGSTAGE = ["Mittwoch", "Sonntag"]

uebungen = [
    {
        "name": "Liegestütz",
        "ziel": "Brust, Schulter, Trizeps, Rumpf",
        "umfang": "8–15 Wiederholungen",
        "ausfuehrung":
            "Hände etwa schulterbreit aufsetzen. Körper von Kopf bis Ferse "
            "in einer Linie halten. Kontrolliert absenken und wieder hochdrücken.",
        "bild": "bilder/liegestuetz.jpg",
        "icon": "💪"
    },
    {
        "name": "Bird Dog",
        "ziel": "Rumpfstabilität, Rücken, Gesäß",
        "umfang": "8–10 je Seite",
        "ausfuehrung":
            "Im Vierfüßlerstand rechten Arm und linkes Bein langsam ausstrecken. "
            "Becken stabil halten. Zurückführen und Seite wechseln.",
        "bild": "bilder/bird_dog.jpg",
        "icon": "🐕"
    },
    {
        "name": "Kniebeuge",
        "ziel": "Oberschenkel, Gesäß, Rumpf",
        "umfang": "12–15 Wiederholungen",
        "ausfuehrung":
            "Füße etwa schulterbreit. Gesäß nach hinten und unten führen. "
            "Knie in Richtung der Fußspitzen halten. Kontrolliert wieder aufrichten.",
        "bild": "bilder/kniebeuge.jpg",
        "icon": "🦵"
    },
    {
        "name": "Side Plank",
        "ziel": "Seitliche Bauchmuskulatur, Rumpfstabilität",
        "umfang": "20–30 Sekunden je Seite",
        "ausfuehrung":
            "Seitlich auf Unterarm und Fuß abstützen. Becken anheben, "
            "bis Schulter, Hüfte und Fuß möglichst eine Linie bilden.",
        "bild": "bilder/side_plank.jpg",
        "icon": "↔️"
    },
    {
        "name": "Glute Bridge",
        "ziel": "Gesäß, hintere Oberschenkel, Rücken",
        "umfang": "12–15 Wiederholungen",
        "ausfuehrung":
            "Rückenlage, Knie gebeugt. Becken durch Anspannen des Gesäßes anheben. "
            "Oben kurz halten und langsam wieder absenken.",
        "bild": "bilder/glute_bridge.jpg",
        "icon": "🌉"
    },
    {
        "name": "Plank",
        "ziel": "Bauch und gesamte Rumpfmuskulatur",
        "umfang": "30–45 Sekunden",
        "ausfuehrung":
            "Auf Unterarmen und Fußspitzen abstützen. Bauch aktiv anspannen. "
            "Kopf, Rücken und Beine möglichst in einer geraden Linie halten.",
        "bild": "bilder/plank.jpg",
        "icon": "▬"
    },
    {
        "name": "Back Step",
        "ziel": "Beine, Gesäß, Gleichgewicht",
        "umfang": "8–10 je Seite",
        "ausfuehrung":
            "Aus dem aufrechten Stand einen kontrollierten Schritt nach hinten machen. "
            "Beide Knie beugen, anschließend über das vordere Bein zurück in den Stand.",
        "bild": "bilder/back_step.jpg",
        "icon": "🔙"
    },
]

dehnungen = [
    {
        "name": "Hüftbeuger",
        "dauer": "30–45 Sekunden je Seite",
        "text":
            "Halbkniestand. Becken leicht nach vorne schieben, ohne ins Hohlkreuz "
            "zu gehen. Dehnung vorne an Hüfte und Oberschenkel spüren."
    },
    {
        "name": "Oberschenkelrückseite",
        "dauer": "30–45 Sekunden je Seite",
        "text":
            "Ein Bein nach vorne ausstrecken. Rücken möglichst gerade halten und "
            "Oberkörper langsam nach vorne neigen."
    },
    {
        "name": "Gesäß",
        "dauer": "30–45 Sekunden je Seite",
        "text":
            "In Rückenlage einen Fuß auf das gegenüberliegende Knie legen und "
            "das andere Bein langsam zum Körper ziehen."
    },
    {
        "name": "Brust und Schulter",
        "dauer": "30–45 Sekunden je Seite",
        "text":
            "Arm seitlich an Wand oder Türrahmen anlegen und Oberkörper "
            "kontrolliert von der Wand wegdrehen."
    },
    {
        "name": "Rücken",
        "dauer": "30–45 Sekunden",
        "text":
            "Aus dem Vierfüßlerstand das Gesäß langsam Richtung Fersen führen "
            "und Arme weit nach vorne strecken."
    },
    {
        "name": "Pezziball",
        "dauer": "30–60 Sekunden",
        "text":
            "Pezziball-Dehnung. Die genaue von Ihnen gewünschte Ausführung "
            "tragen wir anschließend hier ein."
    },
]


# --------------------------------------------------
# Hilfsfunktion Bild
# --------------------------------------------------

def bild_anzeigen(pfad, icon):
    if Path(pfad).exists():
        st.image(pfad, use_container_width=True)
    else:
        st.markdown(
            f"<div style='font-size:70px;text-align:center'>{icon}</div>",
            unsafe_allow_html=True
        )


# --------------------------------------------------
# Status
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

    heute = datetime.now().strftime("%A")

    st.info(
        "3 Runden • 7 Übungen\n\n"
        "Im Anschluss kann die Dehnung separat gestartet werden."
    )

    st.markdown("### Trainingsablauf")

    for nummer, u in enumerate(uebungen, 1):
        st.write(f"**{nummer}. {u['name']}** – {u['umfang']}")

    st.markdown("---")

    if st.button(
        "▶️ Zirkeltraining starten",
        type="primary",
        use_container_width=True
    ):
        st.session_state.runde = 1
        st.session_state.uebung = 0
        st.session_state.seite = "zirkel"
        st.rerun()

    if st.button(
        "🧘 Dehnung",
        use_container_width=True
    ):
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

    fortschritt = (
        ((runde - 1) * len(uebungen) + nr)
        / (3 * len(uebungen))
    )

    st.progress(fortschritt)

    st.header(f"{u['icon']} {u['name']}")

    bild_anzeigen(u["bild"], u["icon"])

    st.markdown(f"### {u['umfang']}")
    st.write(f"**Trainiert:** {u['ziel']}")

    st.info(u["ausfuehrung"])

    st.markdown("---")

    if st.button(
        "✅ Fertig – nächste Übung",
        type="primary",
        use_container_width=True
    ):

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
# ZIRKEL BEENDET
# --------------------------------------------------

elif st.session_state.seite == "zirkel_fertig":

    st.title("✅ Zirkel geschafft")

    st.success(
        "3 Runden vollständig absolviert."
    )

    st.markdown("### Jetzt sinnvoll: Dehnung")

    if st.button(
        "🧘 Dehnung starten",
        type="primary",
        use_container_width=True
    ):
        st.session_state.seite = "dehnung"
        st.rerun()

    if st.button(
        "⌂ Zur Startseite",
        use_container_width=True
    ):
        st.session_state.seite = "start"
        st.rerun()


# --------------------------------------------------
# DEHNUNG
# --------------------------------------------------

elif st.session_state.seite == "dehnung":

    st.title("🧘 Dehnung")

    st.write(
        "Die Dehnung ist bewusst ein **eigenständiger Programmteil** "
        "und kann jederzeit separat aufgerufen werden."
    )

    for nr, d in enumerate(dehnungen, 1):

        with st.expander(
            f"{nr}. {d['name']} – {d['dauer']}",
            expanded=False
        ):
            st.write(d["text"])

    st.markdown("---")

    if st.button(
        "✅ Dehnung beendet",
        type="primary",
        use_container_width=True
    ):
        st.session_state.seite = "start"
        st.rerun()
