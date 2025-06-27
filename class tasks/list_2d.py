def main():
    scores = [[78, 45, 70, 59], [33, 80, 56, 47], [54, 20, 67]]
    for index, score in enumerate(scores):
        for inner_index, inner_value in enumerate(score):
            print(f"inner value: ", inner_value, end = '\t')
            print(f"inner value: ", inner_value)
            print(f"inner list: ", score, end = '\t')
            print(f"inner list index: ", index)


if __name__ == '__main__':
    main()