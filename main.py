from arg_parser import parse_args
from fetch_data import RedditFetcher
from data_processing import FilterPost, PostIterator, PostGenerator, PostZipper
from export_data import CSVExporter, PDFExporter


def main():
    args = parse_args()
    name = args.name
    limit = args.limit
    score = args.score

    # fetching the posts
    fetcher = RedditFetcher()
    print(f"📥 Fetching posts from r/{name}...")
    raw_posts = fetcher.fetch_posts(name, limit)

    # Filtering the posts
    filter_obj = FilterPost(score)
    filtered_posts = filter_obj.filter_post(raw_posts)

    # Generator
    print("Using Generator")
    generator = PostGenerator(filtered_posts)
    generated = list(generator.post_generator())
    for post in generated:
        print(f"{post.title} | Score: {post.score}")

    # Iterator
    print("\nUsing Iterator")
    for post in PostIterator(filtered_posts):
        print(f"{post.title} | Score: {post.score}")

    # Zipping (title + URL)
    zipper = PostZipper(filtered_posts)
    zipped = zipper.zip_title_url()

    print("\n🔗 Top 5 Titles and URLs:")
    for title, url in zipped[:5]:
        print(f"• {title[:60]}... → {url}")

    # Export
    CSVExporter().export(filtered_posts)
    PDFExporter().export(filtered_posts)

    print("\n✅ Done! Exported to posts.csv and posts.pdf.")


if __name__ == "__main__":
    main()
