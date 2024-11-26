class Candidate:
    def __init__(self, ID, name, math_score, physic_score, chemistry_score):
        self.ID = ID
        self.name = name
        self.math_score = math_score
        self.physic_score = physic_score
        self.chemistry_score = chemistry_score
    
    def get_region_priority(self):
        return ID[-2]
    
    def total_score(self):
        if self.get_region_priority() == '1':
            return math_score + physic_score + chemistry_score + 0.5
        if self.get_region_priority() == '2':
            return math_score + physic_score + chemistry_score + 1
        if self.get_region_priority() == '3':
            return math_score + physic_score + chemistry_score + 2.5
        else:
            return math_score + physic_score + chemistry_score
    
    def admission_status(self):
        if self.total_score() >= 24:
            return "DO"
        else:
            return "TRUOT"

    def __str__(self):
        return f'{self.ID} {self.name} {self.get_region_priority()} {self.total_score():.1f} {self.admission_status()}'    


if __name__ == '__main__':
    ID = input()
    name = input()
    math_score = float(input())
    physic_score = float(input())
    chemistry_score = float(input())
    candidate = Candidate(ID, name, math_score, physic_score, chemistry_score)
    print(candidate)
