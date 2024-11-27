#Find the Highest Value
scores = {"Shivansh": 85, "Rahul": 92, "Priya": 89}

max_score = max(scores.values())
top_scorer = [name for name, score in scores.items() if score == max_score]

print("Top Scorer(s):", top_scorer, "with score:", max_score)
