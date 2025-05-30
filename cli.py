import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from song_recommendation_generator import song_recommendation_generator

def load_data():
    
    df = pd.read_csv('dataset.csv')  

    features = [
        'danceability', 'energy', 'key', 'loudness', 'mode',
        'speechiness', 'acousticness', 'instrumentalness',
        'liveness', 'valence', 'tempo'
    ]

    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])

    return df, X

def main():
    print("Welcome to the Song Recommendation Generator!\nEnjoying Music, Made Easier\n")

    df, features_scaled = load_data()

    song_title = input("Enter the song title: ")
    artist_name = input("Enter the artist name: ")

    try:
        recs = song_recommendation_generator(
            df=df,
            features_scaled=features_scaled,
            track_name=song_title,
            artist=artist_name,
            top_n=20
        )
        print("\nHere are your top 20 most similar tracks:\n")
        print(recs[['track_name','artist(s)','track_genre','similarity']].to_string(index=False))
        
        while True:
            save = input("\nWould you like to save this to a CSV file? (Y/N): ").strip().lower()
            if save in ('y', 'n'):
                break
            print("❌ Invalid input! Please enter 'Y' or 'N'.")

        if save == 'y':
            output_path = 'recommendations.csv'
            recs.to_csv(output_path, index=False)
            print(f"✅ Saved recommendations to {output_path}")
        else:
            print("Okay, not saving to CSV.")
      
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
