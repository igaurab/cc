from cli import args
from stats.stats import LineCount, WordsCount, CharCount, ByteCount, FileStatistics

file_content = args.file_content

file_stats = FileStatistics()

file_stats.add_statistic(LineCount()) if args.line else None
file_stats.add_statistic(WordsCount()) if args.words else None
file_stats.add_statistic(CharCount()) if args.characters else None
file_stats.add_statistic(ByteCount()) if args.count else None

if not any(args.flags):
    file_stats.add_statistic(LineCount())
    file_stats.add_statistic(WordsCount())
    file_stats.add_statistic(CharCount())
    file_stats.add_statistic(ByteCount())

for line in file_content():
    file_stats.process_line(line)

result = file_stats.get_results()
print(result)
