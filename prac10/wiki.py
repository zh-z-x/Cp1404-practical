import wikipedia

def main():
    print("Wikipedia Search (Press Enter to quit)")
    search_phrase = input("Enter page title: ").strip()

    while search_phrase != "":
        # Determine if it is a disambiguation page
        search_results = wikipedia.search(search_phrase)
        if not search_results:
            print(f'Page id "{search_phrase}" does not match any pages. Try another id!')
        else:
            # Get the title of the first page
            page_title = search_results[0]
            # Check if the search term matches exactly with the first result; if not, prompt the user for more specific content
            if search_phrase.lower() != page_title.lower():
                print("We need a more specific title. Try one of the following, or a new search:")
                print(search_results[:5])  # Display the top 5 suggested results
            else:
                page = wikipedia.page(page_title, auto_suggest=False)
                summary = wikipedia.summary(page_title, auto_suggest=False)
                print(f"\n{page.title}")
                print(summary)
                print(page.url)

        search_phrase = input("\nEnter page title: ").strip()

    print("Thank you.")

if __name__ == '__main__':
    main()
