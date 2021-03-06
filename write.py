"""
Cavalier Machine Learning, University of Virginia
September 2018

Script for outputting a new pdf/book from scratch. Parameters
can be adjusted through command line args.
"""
from articanon import Articanon
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--k', default=5, type=int)
parser.add_argument('--chapters', default=2, type=int)
parser.add_argument('--verses', default=3, type=int)
parser.add_argument('--filter', choices=['True','False'], default='False', type=str)
args = parser.parse_args()

if __name__ == "__main__":
    articanon = Articanon()
    model = articanon.model
    model.load_weights('./model_saves/articanon_best.h5f')

    for chap in range(args.chapters):
        print("\nGenerating chapter {}...".format(chap+1))
        articanon.generate_chapter_beam(nb_verse=args.verses,
                                    k=args.k,
                                    output_path='./output/chapter{}.txt'.format(chap+1), delete_first=True)
    
    chapter_list = []
    for chap in range(args.chapters):
        filename = './output/chapter{}.txt'.format(chap+1)
        if args.filter == 'True':
            articanon.filter_verses(filename)
        chapter_list.append((filename, articanon.new_chapter_title()))

    articanon.assemble_book(chapter_list, output_path='output/articanon.pdf')
