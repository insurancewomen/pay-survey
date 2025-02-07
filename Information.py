import streamlit as st

st.set_page_config(page_title="IW Parental Leave Survey", page_icon="🧊")

st.write("# InsuranceWomen Parental Leave Survey Results")

st.markdown("""
            Welcome to the InsuranceWomen Parental Leave Study. This
            resource features **user-submitted** data on parental leave policies
            from companies in the insurance industry around the world.

            Applying or interviewing for a new job can be challenging,
            especially if you're planning to start or grow a family. Many
            individuals are hesitant to ask about parental leave policies during
            the hiring process, as there's often a concern that employers may be
            reluctant to hire those who might take leave in the near future
            (despite this being illegal and just a bit of a dick move generally!).

            To help address this, I've created a survey that gathers user data
            (such as gender, country, and type of company) alongside detailed
            policy information (including the length of leave, pay, and other
            benefits). The results are made available in a searchable table,
            allowing you to filter by country, company, and various other
            factors to find the information you need.
            """)

st.page_link(
    "pages/01_🗳️_Results_Table.py",
    label="Click here to see the results",
    icon=":material/table_view:",
)

st.markdown("""
            I hope this study will serve as a living document that will be
            continually updated as policies change. If your company is not
            listed, please click the link below to take the survey! After you've
            completed it, please forward the link to your insurance industry
            pals.
            """)

st.link_button(
    "Take the Survey",
    "https://forms.gle/cXHLYn26WNC9pXks8",
    icon=":material/inventory:",
)

st.warning(
    """
    I am happy to work with companies to ensure that the information is accurate
    and up-to-date. If you're a company representative and would like to provide
    information about your parental leave policy, please reach out to me on
    Instagram. Please note that I will require evidence of the policy in order
    to mark it as verified - but that it will then get a very special badge /
    place in the app to distinguish it from the other responses.
    """,
    icon=":material/warning:",
)


st.link_button(
    "InsuranceWomen on Instagram",
    "https://www.instagram.com/insurancewomen/",
    icon=":material/chat:",
)

st.markdown("""
            This work is [openly licensed via CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/). Non commercial use is forbidden, and any other use must credit
            Insurance Women.
            """)

st.html(
    """
    <a href='https://creativecommons.org/licenses/by-nc/4.0/' target='_blank'>
        <img src='app/static/by-nc.png' alt='Creative Commons Non Commercial badge' width='100'/>
    </a>
    """
)
