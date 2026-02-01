#!/usr/bin/env python3
"""
BFI-44 Personality Test Scoring Script
Calculates Big Five personality traits from agent responses
"""

import sys

def score_bfi(responses_str):
    """
    Score BFI-44 responses and calculate Big Five traits

    Args:
        responses_str: Comma-separated string of 44 ratings (1-5)

    Returns:
        Dict of trait scores and interpretations
    """
    # Parse responses
    try:
        responses = [int(x.strip()) for x in responses_str.split(',')]
    except ValueError:
        print("Error: All responses must be integers 1-5")
        sys.exit(1)

    if len(responses) != 44:
        print(f"Error: Expected 44 responses, got {len(responses)}")
        print("Format: 1,2,3,4,5,...,44")
        sys.exit(1)

    # Validate range
    if not all(1 <= r <= 5 for r in responses):
        print("Error: All ratings must be between 1 and 5")
        sys.exit(1)

    # Reverse-score items marked with (R)
    reverse_items = [6, 21, 31, 2, 12, 27, 37, 8, 18, 23, 9, 24, 34, 35, 41]

    scored = []
    for i, score in enumerate(responses, start=1):
        if i in reverse_items:
            scored.append(6 - score)  # Reverse: 1→5, 2→4, 3→3, 4→2, 5→1
        else:
            scored.append(score)

    # Calculate trait scores (mean of items per trait)
    # Item numbers correspond to BFI-44 standard inventory
    traits = {
        'Extraversion': [scored[i-1] for i in [1, 6, 11, 16, 21, 26, 31, 36]],
        'Agreeableness': [scored[i-1] for i in [2, 7, 12, 17, 22, 27, 32, 37, 42]],
        'Conscientiousness': [scored[i-1] for i in [3, 8, 13, 18, 23, 28, 33, 38, 43]],
        'Neuroticism': [scored[i-1] for i in [4, 9, 14, 19, 24, 29, 34, 39]],
        'Openness': [scored[i-1] for i in [5, 10, 15, 20, 25, 30, 35, 40, 41, 44]]
    }

    # Calculate means and interpretations
    results = {}
    print("\n" + "="*50)
    print("Big Five Personality Results")
    print("="*50)

    for trait, scores in traits.items():
        mean_score = sum(scores) / len(scores)

        # Interpret score
        if mean_score < 2.5:
            interpretation = "Low"
        elif mean_score < 3.5:
            interpretation = "Moderate"
        else:
            interpretation = "High"

        results[trait] = {
            'score': round(mean_score, 2),
            'interpretation': interpretation
        }

        # Print formatted result
        print(f"{trait:20} {mean_score:.2f}  ({interpretation})")

    print("="*50)
    print("\nScore Range: 1.0 - 5.0")
    print("Interpretations: <2.5 = Low | 2.5-3.5 = Moderate | >3.5 = High")
    print("\nBased on BFI-44 (Big Five Inventory)")
    print("="*50 + "\n")

    return results


def main():
    if len(sys.argv) != 2:
        print("BFI-44 Personality Test Scoring")
        print("="*50)
        print("\nUsage:")
        print('  python3 score.py "1,2,3,4,5,...,44"')
        print("\nExample:")
        print('  python3 score.py "4,2,5,3,4,2,5,3,4,5,4,3,2,4,5,3,4,2,3,4,5,4,3,2,4,5,3,4,2,5,3,4,5,3,4,5,4,3,2,4,5,4,3,2"')
        print("\nExpects 44 comma-separated ratings (1-5)")
        print("="*50)
        sys.exit(1)

    score_bfi(sys.argv[1])


if __name__ == "__main__":
    main()
