from src.main.models.labour import Labour,logger



class Mistri(Labour):
    def __init__(self, first_name, last_name, wage, role,skill):
        super().__init__(first_name, last_name, wage, role)
        self.skill = skill
        self.__save_to_skill_table()

    def __save_to_skill_table(self):
        insert_query = """ INSERT INTO skills(labour_id,skill)
                           VALUES(%s,%s)
                         """
        for skill in self.skill:
            self.crud.insert_from_pos(insert_query,(self.id,skill))
            logger.info(f"Skill '{skill}' saved for labour ID {self.id}")

    def to_dict(self):
        data = super().to_date()
        data.update({"skill":self.skill})
        return data