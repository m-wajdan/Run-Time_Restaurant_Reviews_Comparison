import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
def compare(df1, df2):   
    # Ensure 'OverAll' column is numeric, invalid values will be replaced with NaN
    df1['OverAll'] = pd.to_numeric(df1['OverAll'], errors='coerce')
    df2['OverAll'] = pd.to_numeric(df2['OverAll'], errors='coerce')

    avg_csv = df1['OverAll'].mean() 
    avg_scraped = df2['OverAll'].mean() 

    st.markdown(f"""
    **Interpretation:**
    - **Average Overall Rating (CSV):** {avg_csv:.2f}
    - **Average Overall Rating (Scraped):** {avg_scraped:.2f}

    Based on the averages, we can conclude that:
    - If the CSV average is higher, the reviews in the CSV dataset are generally more positive.
    - If the Scraped average is higher, the scraped reviews are more positive.

    """)
def plot_bar_and_scatter_subplots(data_frame1, data_frame2, n):
    """Plot subplots for bar graph and scatter plot separately for both data frames."""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    # Bar Graph for Scraped Data
    bar_width = 0.35
    indices1 = range(len(data_frame1))
    axes[0, 0].bar(indices1, data_frame1["OverAll"], bar_width, color='blue', label="Scraped Data")
    axes[0, 0].set_xticks(indices1)
    axes[0, 0].set_xticklabels(data_frame1["Date"], rotation=90)
    axes[0, 0].set_title("Bar Graph: Overall Ratings (Scraped Data)")
    axes[0, 0].set_xlabel("Date")
    axes[0, 0].set_ylabel("Overall Rating")
    axes[0, 0].legend()

    # Bar Graph for CSV Data
    indices2 = range(len(data_frame2[:n]))
    axes[0, 1].bar(indices2, data_frame2["OverAll"][:n], bar_width, color='orange', label="CSV Data")
    axes[0, 1].set_xticks(indices2)
    axes[0, 1].set_xticklabels(data_frame2["Date"][:n], rotation=90)
    axes[0, 1].set_title("Bar Graph: Overall Ratings (CSV Data)")
    axes[0, 1].set_xlabel("Date")
    axes[0, 1].set_ylabel("Overall Rating")
    axes[0, 1].legend()

    # Scatter Plot for Scraped Data
    axes[1, 0].scatter(data_frame1["Date"], data_frame1["OverAll"], color='blue', label="Scraped Data")
    axes[1, 0].set_xticks(data_frame1["Date"])
    axes[1, 0].tick_params(axis='x', rotation=90)
    axes[1, 0].set_title("Scatter Plot: Overall Ratings (Scraped Data)")
    axes[1, 0].set_xlabel("Date")
    axes[1, 0].set_ylabel("Overall Rating")
    axes[1, 0].legend()

    # Scatter Plot for CSV Data
    axes[1, 1].scatter(data_frame2["Date"][:n], data_frame2["OverAll"][:n], color='orange', label="CSV Data")
    axes[1, 1].set_xticks(data_frame2["Date"][:n])
    axes[1, 1].tick_params(axis='x', rotation=90)
    axes[1, 1].set_title("Scatter Plot: Overall Ratings (CSV Data)")
    axes[1, 1].set_xlabel("Date")
    axes[1, 1].set_ylabel("Overall Rating")
    axes[1, 1].legend()

    plt.tight_layout()
    st.pyplot(fig)

        
def plot_ratings(url, n):
    from GetReviews import DataScrapping


    data_frame1 = DataScrapping(url, n)
    data_frame = pd.read_csv("restaurant_reviews_data.csv")

    data_frame1["differentDate"] = data_frame1["Date"] + " #" + (data_frame1.index + 1).astype(str)
    data_frame["differentDate"] = data_frame["Date"][:n] + " #" + (data_frame.index[:n] + 1).astype(str)

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    axes[0].plot(data_frame["differentDate"][:n], data_frame["OverAll"][:n], label="Overall Ratings")
    axes[0].set_xticks(data_frame["differentDate"][:n])  
    axes[0].tick_params(axis='x', rotation=90)  
    axes[0].legend()
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Overall Rating")
    axes[0].set_title("Date vs Overall Rating (CSV)")

    axes[1].plot(data_frame1["differentDate"], data_frame1["OverAll"], label="Overall Ratings (Scraped)")
    axes[1].set_xticks(data_frame1["differentDate"])  
    axes[1].tick_params(axis='x', rotation=90)  
    axes[1].legend()
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel("Overall Rating")
    axes[1].set_title("Date vs Overall Rating (Scraped)")

    plt.tight_layout()
    st.pyplot(fig)
    compare(data_frame1,data_frame)
    plot_bar_and_scatter_subplots(data_frame1, data_frame,n)
#-----------------------------------------------BONUS PART-------------------------------------------------------
def plot_overall(data_frame1, data_frame, n):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    data_frame1["differentDate"] = data_frame1["Date"] + " #" + (data_frame1.index + 1).astype(str)
    data_frame["differentDate"] = data_frame["Date"][:n] + " #" + (data_frame.index[:n] + 1).astype(str)

    axes[0].plot(data_frame1['Date'][:n], data_frame1['OverAll'][:n], label='AssignedRestaurant', color='blue', marker='o')
    axes[0].set_title('OverAll vs Date (AssignedRestaurant)')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('OverAll')
    axes[0].tick_params(axis='x', rotation=90, labelsize='small')  
    axes[0].legend(loc='upper right')

    axes[1].plot(data_frame['Date'][:n], data_frame['OverAll'][:n], label='NewRestaurant', color='green', marker='x')
    axes[1].set_title('OverAll vs Date (NewRestaurant)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('OverAll')
    axes[1].tick_params(axis='x', rotation=90, labelsize='small')  

    plt.tight_layout()
    st.pyplot(fig)

def plot_food(data_frame1, data_frame, n):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6)) 

    data_frame1["differentDate"] = data_frame1["Date"] + " #" + (data_frame1.index + 1).astype(str)
    data_frame["differentDate"] = data_frame["Date"][:n] + " #" + (data_frame.index[:n] + 1).astype(str)

    axes[0].plot(data_frame1['Date'][:n], data_frame1['Food'][:n], label='AssignedRestaurant', color='blue', marker='o')
    axes[0].set_title('Food vs Date (AssignedRestaurant)')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Food')
    axes[0].tick_params(axis='x', rotation=90, labelsize='small')  
    axes[0].legend(loc='upper right')

    axes[1].plot(data_frame['Date'][:n], data_frame['Food'][:n], label='NewRestaurant', color='green', marker='x')
    axes[1].set_title('Food vs Date (NewRestaurant)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Food')
    axes[1].tick_params(axis='x', rotation=90, labelsize='small') 
    axes[1].legend(loc='upper right')

    plt.tight_layout()
    st.pyplot(fig)

def plot_service(data_frame1, data_frame, n):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))  

    data_frame1["differentDate"] = data_frame1["Date"] + " #" + (data_frame1.index + 1).astype(str)
    data_frame["differentDate"] = data_frame["Date"][:n] + " #" + (data_frame.index[:n] + 1).astype(str)

    axes[0].plot(data_frame1['Date'][:n], data_frame1['Service'][:n], label='AssignedRestaurant', color='blue', marker='o')
    axes[0].set_title('Service vs Date (AssignedRestaurant)')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Service')
    axes[0].tick_params(axis='x', rotation=90, labelsize='small')  
    axes[0].legend(loc='upper right')

   
    axes[1].plot(data_frame['Date'][:n], data_frame['Service'][:n], label='NewRestaurant', color='green', marker='x')
    axes[1].set_title('Service vs Date (NewRestaurant)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Service')
    axes[1].tick_params(axis='x', rotation=90, labelsize='small') 
    axes[1].legend(loc='upper right')

   
    plt.tight_layout()
    st.pyplot(fig)


def plot_ambience(data_frame1, data_frame, n):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6)) 

    data_frame1["differentDate"] = data_frame1["Date"] + " #" + (data_frame1.index + 1).astype(str)
    data_frame["differentDate"] = data_frame["Date"][:n] + " #" + (data_frame.index[:n] + 1).astype(str)
   
    axes[0].plot(data_frame1['Date'][:n], data_frame1['Ambience'][:n], label='AssignedRestaurant', color='blue', marker='o')
    axes[0].set_title('Ambience vs Date (AssignedRestaurant)')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Ambience')
    axes[0].tick_params(axis='x', rotation=90, labelsize='small')  
    axes[0].legend(loc='upper right')

    axes[1].plot(data_frame['Date'][:n], data_frame['Ambience'][:n], label='NewRestaurant', color='green', marker='x')
    axes[1].set_title('Ambience vs Date (NewRestaurant)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Ambience')
    axes[1].tick_params(axis='x', rotation=90, labelsize='small') 
    axes[1].legend(loc='upper right')

    
    plt.tight_layout()
    st.pyplot(fig)
#-----------------------------------------------BONUS PART-------------------------------------------------------
def plot_overall_violin(data_frame1, data_frame, n):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))  

    sns.violinplot(x=data_frame1['Date'][:n], y=data_frame1['OverAll'][:n], ax=axes[0], color='blue')
    axes[0].set_title('OverAll Distribution (DataFrame1)')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('OverAll')
    axes[0].tick_params(axis='x', rotation=90, labelsize='small')  

    sns.violinplot(x=data_frame['Date'][:n], y=data_frame['OverAll'][:n], ax=axes[1], color='green')
    axes[1].set_title('OverAll Distribution (DataFrame)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('OverAll')
    axes[1].tick_params(axis='x', rotation=90, labelsize='small') 

    plt.tight_layout()
    st.pyplot(fig)

def plot_food_violin(data_frame1, data_frame, n):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6)) 

    sns.violinplot(x=data_frame1['Date'][:n], y=data_frame1['Food'][:n], ax=axes[0], color='blue')
    axes[0].set_title('Food Distribution (DataFrame1)')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Food')
    axes[0].tick_params(axis='x', rotation=90, labelsize='small')  

    sns.violinplot(x=data_frame['Date'][:n], y=data_frame['Food'][:n], ax=axes[1], color='green')
    axes[1].set_title('Food Distribution (DataFrame)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Food')
    axes[1].tick_params(axis='x', rotation=90, labelsize='small') 

    plt.tight_layout()
    st.pyplot(fig)

def plot_service_violin(data_frame1, data_frame, n):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    sns.violinplot(x=data_frame1['Date'][:n], y=data_frame1['Service'][:n], ax=axes[0], color='blue')
    axes[0].set_title('Service Distribution (DataFrame1)')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Service')
    axes[0].tick_params(axis='x', rotation=90, labelsize='small')  

    sns.violinplot(x=data_frame['Date'][:n], y=data_frame['Service'][:n], ax=axes[1], color='green')
    axes[1].set_title('Service Distribution (DataFrame)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Service')
    axes[1].tick_params(axis='x', rotation=90, labelsize='small')  

    plt.tight_layout()
    st.pyplot(fig)

def plot_ambience_violin(data_frame1, data_frame, n):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))  
    sns.violinplot(x=data_frame1['Date'][:n], y=data_frame1['Ambience'][:n], ax=axes[0], color='blue')
    axes[0].set_title('Ambience Distribution (DataFrame1)')
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Ambience')
    axes[0].tick_params(axis='x', rotation=90, labelsize='small')

    sns.violinplot(x=data_frame['Date'][:n], y=data_frame['Ambience'][:n], ax=axes[1], color='green')
    axes[1].set_title('Ambience Distribution (DataFrame)')
    axes[1].set_xlabel('Date')
    axes[1].set_ylabel('Ambience')
    axes[1].tick_params(axis='x', rotation=90, labelsize='small') 

    plt.tight_layout()
    st.pyplot(fig)

    



def bonusPlots(url,n):
    from GetReviews import DataScrapping
    data_frame1 = DataScrapping(url, n)
    data_frame = pd.read_csv("restaurant_reviews_data.csv")
        
    data_frame1["differentDate"] = data_frame1["Date"] + " #" + (data_frame1.index + 1).astype(str)
    data_frame["differentDate"] = data_frame["Date"][:n] + " #" + (data_frame.index[:n] + 1).astype(str)

    plot_overall(data_frame,data_frame1,n)
    plot_food(data_frame,data_frame1,n)
    plot_ambience(data_frame,data_frame1,n)
    plot_service(data_frame,data_frame1,n)

    # plt_Violin for both data frames
    # plot_overall_violin(data_frame1, data_frame, n)
    # plot_food_violin(data_frame1, data_frame, n)
    # plot_service_violin(data_frame1, data_frame, n)
    # plot_ambience_violin(data_frame1, data_frame, n)
#-----------------------------------------------BONUS PART-------------------------------------------------------




# Function to convert an image to a Base64 string
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Load the Base64 image
image_base64 = get_base64_image("image.jpg")

# Set page configuration
st.set_page_config(page_title="Magic Hour Rooftop Bar & Lounge", layout="wide")

# Custom CSS for enhanced styling
st.markdown(
    f"""
    <style>
        body {{
            background-color: #fef6e4;
            font-family: 'Georgia', serif;
        }}
        .header-container {{
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;    
        }}
        .header-container img {{
            width: 100%;
            max-width: 1200px;
            height: auto;
            border: 5px solid #FF5733;
            border-radius: 20px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.5);
        }}
        .header-container h1 {{
            color: #FF5733;
            font-size: 3.5em;
        }}
        .navbar {{
            background-color: #FF5733;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
        }}
        .navbar a {{
            color: white;
            text-decoration: none;
            font-size: 1.2em;
            margin: 0 25px;
            font-weight: bold;
        }}
        .navbar a:hover {{
            color: #fef6e4;
        }}
        .review-container {{
            background-color: #000000;
            padding: 15px;
            margin: 15px 0;
            border-radius: 10px;
            color: white;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }}
        .review-header {{
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }}
        .review-header img {{
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 15px;
        }}
        .review-header h4 {{
            margin: 0;
            color: white;
        }}
        .review-header p {{
            margin: 0;
            font-size: 1.2em;
            color: gold;
        }}
        .review-ratings {{
            margin: 10px 0;
            display: flex;
            gap: 15px;
            font-size: 1em;
            color: white;
        }}
        .review-ratings span {{
            background-color: grey;
            padding: 5px 10px;
            border-radius: 5px;
            font-weight: bold;
            border: 1px solid white;
        }}
        .sidebar-title {{
            font-family: 'Georgia', serif;
            font-size: 1.5em;
            font-weight: bold;
            color: #FF4500;
            text-align: center;
            padding-bottom: 5px;
            border-bottom: 2px solid #FF4500;
            margin-bottom: 15px;
        }}

        .st-radio > label {{
            display: none;
        }}

        .st-radio div[role='radiogroup'] {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}

        .st-radio div[role='radiogroup'] label {{
            font-family: 'Georgia', serif;
            font-size: 1em;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }}

        .st-radio div[role='radiogroup'] label:hover {{
            background-color: #FFF5E5;
            color: #FF4500;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar with custom CSS styling
st.markdown(
    """
    <style>
        .sidebar-title {
            font-family: 'Georgia', serif;
            font-size: 1.5em;
            font-weight: bold;
            color: #FF4500;
            text-align: center;
            padding-bottom: 5px;
            border-bottom: 2px solid #FF4500;
            margin-bottom: 15px;
        }

        .st-radio > label {
            display: none;  /* Hide default label */
        }

        .st-radio div[role='radiogroup'] {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .st-radio div[role='radiogroup'] label {
            font-family: 'Georgia', serif;
            font-size: 1em;
            padding: 10px;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        .st-radio div[role='radiogroup'] label:hover {
            background-color: #FFF5E5;
            color: #FF4500;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation with styled heading
st.sidebar.markdown("<div class='sidebar-title'>Search for:</div>", unsafe_allow_html=True)

selected_action = st.sidebar.radio(
    "",
    ("Home", "Reviews", "Review Analysis", "Compare")
)

# Load the datasets
data_reviews_analysis = pd.read_csv("Reviews_Analysis.csv")
data_restaurant_reviews = pd.read_csv("restaurant_reviews_data.csv")

# Function to generate stars based on the rating
def generate_stars(rating):
    full_star = "★"
    empty_star = "☆"
    return full_star * rating + empty_star * (5 - rating)

# Helper function to highlight parts of the review
def highlight_review_text(review):
    food_keywords = ["food", "dish", "meal", "cuisine", "taste"]
    service_keywords = ["service", "staff", "waiter", "server", "hospitality"]

    for keyword in food_keywords:
        review = review.replace(keyword, f"<span style='color:#FFA07A; font-weight:bold;'>{keyword}</span>")
    for keyword in service_keywords:
        review = review.replace(keyword, f"<span style='color:#87CEEB; font-weight:bold;'>{keyword}</span>")

    return review

# Home page

def render_home_page():
    st.markdown(
        f"""
        <div class="header-container">
            <img src="data:image/png;base64,{image_base64}" alt="Magic Hour Rooftop Bar & Lounge">
            <h1>Welcome to Magic Hour Rooftop Bar & Lounge</h1>
        </div>
        <div style="text-align:center; margin: 20px 0;">
            <p style="font-size: 1.5em; color: #444;">
                Experience the ultimate dining and nightlife destination with breathtaking views, exquisite food, and world-class service.
            </p>
        </div>
        
        <div style="display: flex; justify-content: center; gap: 20px;">
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
                <h3 style="color: #FF5733;">Exclusive Ambience</h3>
                <p>Immerse yourself in our chic and vibrant rooftop setting with stunning city views.</p>
            </div>
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
                <h3 style="color: #FF5733;">Gourmet Delights</h3>
                <p>Savor our carefully curated menu featuring culinary masterpieces for every palate.</p>
            </div>
            <div style="background-color: #000000; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0,0,0,0.2);">
                <h3 style="color: #FF5733;">Top-notch Service</h3>
                <p>Experience exceptional hospitality from our friendly and professional staff.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
   
# Render the selected page
if selected_action == "Home":
    render_home_page()

# Reviews Page
elif selected_action == "Reviews":
    st.markdown("<h2 id='reviews'>Reviews</h2>", unsafe_allow_html=True)
    num_reviews = st.number_input("Number of reviews to display:", min_value=1, max_value=len(data_restaurant_reviews), step=1)
    st.markdown("<h4>Apply Filters:</h4>", unsafe_allow_html=True)
    overall_filter = st.number_input("Filter by Overall Rating:", min_value=0, max_value=10, step=1)
    food_filter = st.number_input("Filter by Food Rating:", min_value=0, max_value=10, step=1)
    service_filter = st.number_input("Filter by Service Rating:", min_value=0, max_value=10, step=1)

    # Apply filters
    filtered_reviews = data_restaurant_reviews[
        (data_restaurant_reviews['OverAll'] >= overall_filter) &
        (data_restaurant_reviews['Food'] >= food_filter) &
        (data_restaurant_reviews['Service'] >= service_filter)
    ].head(num_reviews)  # Limit to the specified number of reviews

    # Display filtered reviews
    for index, row in filtered_reviews.iterrows():
        stars = generate_stars(int(row['OverAll']))
        highlighted_review = highlight_review_text(row['Review'].lower())

        # Path to the user image
        profile_image_path = "user.png" 

        st.markdown(
            f"""
            <div class="review-container" style="background-color: #1b1110; color: white; padding: 10px; border-radius: 8px;">
                <div class="review-header">
                    <img src="data:image/png;base64,{get_base64_image(profile_image_path)}" alt="Profile" style="width: 50px; height: 50px; border-radius: 50%; margin-right: 10px;">
                    <div>
                        <h4>{row['Name']} <span style='font-size: 0.9em; color: gray;'>({row['Date']})</span></h4>
                        <p>{stars}</p> <!-- Display the stars -->
                    </div>
                </div>
                <div class="review-ratings">
                    <span>Overall: {row['OverAll']}</span>
                    <span>Food: {row['Food']}</span>
                    <span>Service: {row['Service']}</span>
                    <span>Ambience: {row['Ambience']}</span>
                </div>
                <p>{highlighted_review}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
elif selected_action == "Review Analysis":
    review_type = st.sidebar.radio("Select Review Type", ("Food Quality", "Staff & Service", "Overall Analysis", "Combined Analysis"))
    
    review_options = list(range(1, 881, 5))  
    if 880 not in review_options:
        review_options.append(880)  

    num_reviews = st.sidebar.selectbox("Select number of reviews to display:", review_options, index=0)  

    if review_type == "Food Quality":
        st.markdown("### Food Quality Reviews")
        food_reviews = data_reviews_analysis[data_reviews_analysis['Food Quality'].notnull()].head(num_reviews)
        for _, row in food_reviews.iterrows():
            st.markdown(
                f"""
                <div style="border:1px solid #FF5733; padding:10px; margin:10px; border-radius:8px; background-color: #000000; color: white;">
                    <p>{row['Food Quality']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


    elif review_type == "Staff & Service":
        st.markdown("### Staff & Service Reviews")
        service_reviews = data_reviews_analysis[data_reviews_analysis['Staff & Service'].notnull()].head(num_reviews)
        for _, row in service_reviews.iterrows():
            st.markdown(
                f"""
                <div style="border:1px solid #FF5733; padding:10px; margin:10px; border-radius:8px; background-color: #000000; color: white;">
                    <p>{row['Staff & Service']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    elif review_type == "Overall Analysis":
        st.markdown("### Overall Analysis Reviews")
        overall_reviews = data_reviews_analysis[data_reviews_analysis['Analysis'].notnull()].head(num_reviews)
        for _, row in overall_reviews.iterrows():
            st.markdown(
                f"""
                <div style="border:1px solid #FF5733; padding:10px; margin:10px; border-radius:8px; background-color: #000000; color: white;">
                    <p>{row['Analysis']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    elif review_type == "Combined Analysis":
        st.markdown("### Combined Analysis")
        combined_reviews = data_reviews_analysis.head(num_reviews)
        for _, row in combined_reviews.iterrows():
            st.markdown(
                f"""
                <div style="border:1px solid #FF5733; padding:10px; margin:10px; border-radius:8px; background-color: #000000; color: white;">
                    <p><b style="color:#FFA07A;">Food Quality:</b> {row['Food Quality'] if pd.notnull(row['Food Quality']) else 'N/A'}</p>
                    <p><b style="color:#87CEEB;">Staff & Service:</b> {row['Staff & Service'] if pd.notnull(row['Staff & Service']) else 'N/A'}</p>
                    <p><b style="color:#FFD700;">Overall Analysis:</b> {row['Analysis'] if pd.notnull(row['Analysis']) else 'N/A'}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

elif selected_action == "Compare":
    st.markdown("<h2 id='compare'>Compare Reviews</h2>", unsafe_allow_html=True)
    url = st.text_input("Enter the URL to scrape reviews:")
    num_reviews = st.number_input("Number of reviews to scrape:", min_value=1, step=1)

    if st.button("Scrape and Display Reviews"):
        if url:
            try:
                with st.spinner('Scraping reviews...'):
                    from GetReviews import DataScrapping
                    scraped_reviews = DataScrapping(url, num_reviews)

                    scraped_df = pd.DataFrame(scraped_reviews, columns=["Name", "Review", "OverAll", "Food", "Service", "Ambience", "Date"])

                    for index, row in scraped_df.iterrows():
                        stars = generate_stars(int(row['OverAll']))
                        highlighted_review = highlight_review_text(row['Review'].lower())

                        st.markdown(
                            f"""
                            <div class="review-container" style="background-color: #1b1110; color: white; padding: 10px; border-radius: 8px;">
                                <div class="review-header">
                                    <img src="data:image/png;base64,{get_base64_image('user.png')}" alt="Profile" style="width: 50px; height: 50px; border-radius: 50%; margin-right: 10px;">
                                    <div>
                                        <h4>{row['Name']} <span style='font-size: 0.9em; color: gray;'>({row['Date']})</span></h4>
                                        <p>{stars}</p> <!-- Display the stars -->
                                    </div>
                                </div>
                                <div class="review-ratings">
                                    <span>Overall: {row['OverAll']}</span>
                                    <span>Food: {row['Food']}</span>
                                    <span>Service: {row['Service']}</span>
                                    <span>Ambience: {row['Ambience']}</span>
                                </div>
                                <p>{highlighted_review}</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid URL.")

    if st.button("Scrape and Display Comparison"):
        if url:
            try:
                with st.spinner('Processing the comparison...'):
                    plot_ratings(url, num_reviews)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid URL.")

    if st.button("BONUSSSSS PARTTTT"):
        if url:
            try:
                with st.spinner('Generating line graph...'):
                    st.header("LineGraph wrt Dates")
                    bonusPlots(url, num_reviews)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid URL.")

                

st.markdown(
    """
    <footer style="text-align:center; margin-top:20px; padding:10px; background-color:#FF5733; color:#fff; border-radius:8px;">
        <p>&copy; 2024 Magic Hour Rooftop Bar & Lounge. All rights reserved.</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
