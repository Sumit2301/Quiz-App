import os
from django.core.management.base import BaseCommand
from quiz.models import Question

class Command(BaseCommand):
    help = 'Load questions from a text file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File "{file_path}" does not exist.'))
            return

        with open(file_path, 'r') as file:
            content = file.read().strip().split('\n\n')  # Split by double newline
            for block in content:
                lines = block.split('\n')
                if len(lines) < 6:
                    self.stdout.write(self.style.ERROR('Invalid format, skipping block.'))
                    continue
                
                question_text = lines[0].replace('Question: ', '').strip()
                options = []
                for i in range(1, 5):
                    options.append(lines[i].replace(f'Option {i}: ', '').strip())
                correct_option = int(lines[5].replace('Correct Answer: ', '').strip())
                
                question = Question(
                    question_text=question_text,
                    option1=options[0],
                    option2=options[1],
                    option3=options[2],
                    option4=options[3],
                    correct_option=correct_option
                )
                question.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully added question: {question_text}'))
