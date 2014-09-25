import sudoku as s
from kivy.app import App

from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty

from kivy.uix.boxlayout import BoxLayout

class MyFirstWidget(BoxLayout):
   
    
    txt_0= ObjectProperty('int')
    txt_1= ObjectProperty('int')
    txt_2= ObjectProperty('int')
    txt_3= ObjectProperty('int')
    txt_4= ObjectProperty('int')
    txt_5= ObjectProperty('int')
    txt_6= ObjectProperty('int')
    txt_7= ObjectProperty('int')
    txt_8= ObjectProperty('int')
    txt_9= ObjectProperty('int')
    txt_10= ObjectProperty('int')
    txt_11= ObjectProperty('int')
    txt_12= ObjectProperty('int')
    txt_13= ObjectProperty('int')
    txt_14= ObjectProperty('int')
    txt_15= ObjectProperty('int')
    txt_16= ObjectProperty('int')
    txt_17= ObjectProperty('int')
    txt_18= ObjectProperty('int')
    txt_19= ObjectProperty('int')
    txt_20= ObjectProperty('int')
    txt_21= ObjectProperty('int')
    txt_22= ObjectProperty('int')
    txt_23= ObjectProperty('int')
    txt_24= ObjectProperty('int')
    txt_25= ObjectProperty('int')
    txt_26= ObjectProperty('int')
    txt_27= ObjectProperty('int')
    txt_28= ObjectProperty('int')
    txt_29= ObjectProperty('int')
    txt_30= ObjectProperty('int')
    txt_31= ObjectProperty('int')
    txt_32= ObjectProperty('int')
    txt_33= ObjectProperty('int')
    txt_34= ObjectProperty('int')
    txt_35= ObjectProperty('int')
    txt_36= ObjectProperty('int')
    txt_37= ObjectProperty('int')
    txt_38= ObjectProperty('int')
    txt_39= ObjectProperty('int')
    txt_40= ObjectProperty('int')
    txt_41= ObjectProperty('int')
    txt_42= ObjectProperty('int')
    txt_43= ObjectProperty('int')
    txt_44= ObjectProperty('int')
    txt_45= ObjectProperty('int')
    txt_46= ObjectProperty('int')
    txt_47= ObjectProperty('int')
    txt_48= ObjectProperty('int')
    txt_49= ObjectProperty('int')
    txt_50= ObjectProperty('int')
    txt_51= ObjectProperty('int')
    txt_52= ObjectProperty('int')
    txt_53= ObjectProperty('int')
    txt_54= ObjectProperty('int')
    txt_55= ObjectProperty('int')
    txt_56= ObjectProperty('int')
    txt_57= ObjectProperty('int')
    txt_58= ObjectProperty('int')
    txt_59= ObjectProperty('int')
    txt_60= ObjectProperty('int')
    txt_61= ObjectProperty('int')
    txt_62= ObjectProperty('int')
    txt_63= ObjectProperty('int')
    txt_64= ObjectProperty('int')
    txt_65= ObjectProperty('int')
    txt_66= ObjectProperty('int')
    txt_67= ObjectProperty('int')
    txt_68= ObjectProperty('int')
    txt_69= ObjectProperty('int')
    txt_70= ObjectProperty('int')
    txt_71= ObjectProperty('int')
    txt_72= ObjectProperty('int')
    txt_73= ObjectProperty('int')
    txt_74= ObjectProperty('int')
    txt_75= ObjectProperty('int')
    txt_76= ObjectProperty('int')
    txt_77= ObjectProperty('int')
    txt_78= ObjectProperty('int')
    txt_79= ObjectProperty('int')
    txt_80= ObjectProperty('int')
    def clear(self):
        self.txt_0.text = ''
        self.txt_1.text = ''
        self.txt_2.text = ''
        self.txt_3.text = ''
        self.txt_4.text = ''
        self.txt_5.text = ''
        self.txt_6.text = ''
        self.txt_7.text = ''
        self.txt_8.text = ''
        self.txt_9.text = ''
        self.txt_10.text = ''
        self.txt_11.text = ''
        self.txt_12.text = ''
        self.txt_13.text = ''
        self.txt_14.text = ''
        self.txt_15.text = ''
        self.txt_16.text = ''
        self.txt_17.text = ''
        self.txt_18.text = ''
        self.txt_19.text = ''
        self.txt_20.text = ''
        self.txt_21.text = ''
        self.txt_22.text = ''
        self.txt_23.text = ''
        self.txt_24.text = ''
        self.txt_25.text = ''
        self.txt_26.text = ''
        self.txt_27.text = ''
        self.txt_28.text = ''
        self.txt_29.text = ''
        self.txt_30.text = ''
        self.txt_31.text = ''
        self.txt_32.text = ''
        self.txt_33.text = ''
        self.txt_34.text = ''
        self.txt_35.text = ''
        self.txt_36.text = ''
        self.txt_37.text = ''
        self.txt_38.text = ''
        self.txt_39.text = ''
        self.txt_40.text = ''
        self.txt_41.text = ''
        self.txt_42.text = ''
        self.txt_43.text = ''
        self.txt_44.text = ''
        self.txt_45.text = ''
        self.txt_46.text = ''
        self.txt_47.text = ''
        self.txt_48.text = ''
        self.txt_49.text = ''
        self.txt_50.text = ''
        self.txt_51.text = ''
        self.txt_52.text = ''
        self.txt_53.text = ''
        self.txt_54.text = ''
        self.txt_55.text = ''
        self.txt_56.text = ''
        self.txt_57.text = ''
        self.txt_58.text = ''
        self.txt_59.text = ''
        self.txt_60.text = ''
        self.txt_61.text = ''
        self.txt_62.text = ''
        self.txt_63.text = ''
        self.txt_64.text = ''
        self.txt_65.text = ''
        self.txt_66.text = ''
        self.txt_67.text = ''
        self.txt_68.text = ''
        self.txt_69.text = ''
        self.txt_70.text = ''
        self.txt_71.text = ''
        self.txt_72.text = ''
        self.txt_73.text = ''
        self.txt_74.text = ''
        self.txt_75.text = ''
        self.txt_76.text = ''
        self.txt_77.text = ''
        self.txt_78.text = ''
        self.txt_79.text = ''
        self.txt_80.text = ''
    def solve(self):
        puzzle = []
        
        puzzle.append(self.txt_0.text)
        puzzle.append(self.txt_1.text)
        puzzle.append(self.txt_2.text)
        puzzle.append(self.txt_3.text)
        puzzle.append(self.txt_4.text)
        puzzle.append(self.txt_5.text)
        puzzle.append(self.txt_6.text)
        puzzle.append(self.txt_7.text)
        puzzle.append(self.txt_8.text)
        puzzle.append(self.txt_9.text)
        puzzle.append(self.txt_10.text)
        puzzle.append(self.txt_11.text)
        puzzle.append(self.txt_12.text)
        puzzle.append(self.txt_13.text)
        puzzle.append(self.txt_14.text)
        puzzle.append(self.txt_15.text)
        puzzle.append(self.txt_16.text)
        puzzle.append(self.txt_17.text)
        puzzle.append(self.txt_18.text)
        puzzle.append(self.txt_19.text)
        puzzle.append(self.txt_20.text)
        puzzle.append(self.txt_21.text)
        puzzle.append(self.txt_22.text)
        puzzle.append(self.txt_23.text)
        puzzle.append(self.txt_24.text)
        puzzle.append(self.txt_25.text)
        puzzle.append(self.txt_26.text)
        puzzle.append(self.txt_27.text)
        puzzle.append(self.txt_28.text)
        puzzle.append(self.txt_29.text)
        puzzle.append(self.txt_30.text)
        puzzle.append(self.txt_31.text)
        puzzle.append(self.txt_32.text)
        puzzle.append(self.txt_33.text)
        puzzle.append(self.txt_34.text)
        puzzle.append(self.txt_35.text)
        puzzle.append(self.txt_36.text)
        puzzle.append(self.txt_37.text)
        puzzle.append(self.txt_38.text)
        puzzle.append(self.txt_39.text)
        puzzle.append(self.txt_40.text)
        puzzle.append(self.txt_41.text)
        puzzle.append(self.txt_42.text)
        puzzle.append(self.txt_43.text)
        puzzle.append(self.txt_44.text)
        puzzle.append(self.txt_45.text)
        puzzle.append(self.txt_46.text)
        puzzle.append(self.txt_47.text)
        puzzle.append(self.txt_48.text)
        puzzle.append(self.txt_49.text)
        puzzle.append(self.txt_50.text)
        puzzle.append(self.txt_51.text)
        puzzle.append(self.txt_52.text)
        puzzle.append(self.txt_53.text)
        puzzle.append(self.txt_54.text)
        puzzle.append(self.txt_55.text)
        puzzle.append(self.txt_56.text)
        puzzle.append(self.txt_57.text)
        puzzle.append(self.txt_58.text)
        puzzle.append(self.txt_59.text)
        puzzle.append(self.txt_60.text)
        puzzle.append(self.txt_61.text)
        puzzle.append(self.txt_62.text)
        puzzle.append(self.txt_63.text)
        puzzle.append(self.txt_64.text)
        puzzle.append(self.txt_65.text)
        puzzle.append(self.txt_66.text)
        puzzle.append(self.txt_67.text)
        puzzle.append(self.txt_68.text)
        puzzle.append(self.txt_69.text)
        puzzle.append(self.txt_70.text)
        puzzle.append(self.txt_71.text)
        puzzle.append(self.txt_72.text)
        puzzle.append(self.txt_73.text)
        puzzle.append(self.txt_74.text)
        puzzle.append(self.txt_75.text)
        puzzle.append(self.txt_76.text)
        puzzle.append(self.txt_77.text)
        puzzle.append(self.txt_78.text)
        puzzle.append(self.txt_79.text)
        puzzle.append(self.txt_80.text)
        for x in range(81):
            if puzzle[x] == '':
                puzzle[x] = '0'
        #print puzzle
        puzzle2=s.Solve2(puzzle)
        #print puzzle2
        self.txt_0.text = puzzle2[0]
        self.txt_1.text = puzzle2[1]
        self.txt_2.text = puzzle2[2]
        self.txt_3.text = puzzle2[3]
        self.txt_4.text = puzzle2[4]
        self.txt_5.text = puzzle2[5]
        self.txt_6.text = puzzle2[6]
        self.txt_7.text = puzzle2[7]
        self.txt_8.text = puzzle2[8]
        self.txt_9.text = puzzle2[9]
        self.txt_10.text = puzzle2[10]
        self.txt_11.text = puzzle2[11]
        self.txt_12.text = puzzle2[12]
        self.txt_13.text = puzzle2[13]
        self.txt_14.text = puzzle2[14]
        self.txt_15.text = puzzle2[15]
        self.txt_16.text = puzzle2[16]
        self.txt_17.text = puzzle2[17]
        self.txt_18.text = puzzle2[18]
        self.txt_19.text = puzzle2[19]
        self.txt_20.text = puzzle2[20]
        self.txt_21.text = puzzle2[21]
        self.txt_22.text = puzzle2[22]
        self.txt_23.text = puzzle2[23]
        self.txt_24.text = puzzle2[24]
        self.txt_25.text = puzzle2[25]
        self.txt_26.text = puzzle2[26]
        self.txt_27.text = puzzle2[27]
        self.txt_28.text = puzzle2[28]
        self.txt_29.text = puzzle2[29]
        self.txt_30.text = puzzle2[30]
        self.txt_31.text = puzzle2[31]
        self.txt_32.text = puzzle2[32]
        self.txt_33.text = puzzle2[33]
        self.txt_34.text = puzzle2[34]
        self.txt_35.text = puzzle2[35]
        self.txt_36.text = puzzle2[36]
        self.txt_37.text = puzzle2[37]
        self.txt_38.text = puzzle2[38]
        self.txt_39.text = puzzle2[39]
        self.txt_40.text = puzzle2[40]
        self.txt_41.text = puzzle2[41]
        self.txt_42.text = puzzle2[42]
        self.txt_43.text = puzzle2[43]
        self.txt_44.text = puzzle2[44]
        self.txt_45.text = puzzle2[45]
        self.txt_46.text = puzzle2[46]
        self.txt_47.text = puzzle2[47]
        self.txt_48.text = puzzle2[48]
        self.txt_49.text = puzzle2[49]
        self.txt_50.text = puzzle2[50]
        self.txt_51.text = puzzle2[51]
        self.txt_52.text = puzzle2[52]
        self.txt_53.text = puzzle2[53]
        self.txt_54.text = puzzle2[54]
        self.txt_55.text = puzzle2[55]
        self.txt_56.text = puzzle2[56]
        self.txt_57.text = puzzle2[57]
        self.txt_58.text = puzzle2[58]
        self.txt_59.text = puzzle2[59]
        self.txt_60.text = puzzle2[60]
        self.txt_61.text = puzzle2[61]
        self.txt_62.text = puzzle2[62]
        self.txt_63.text = puzzle2[63]
        self.txt_64.text = puzzle2[64]
        self.txt_65.text = puzzle2[65]
        self.txt_66.text = puzzle2[66]
        self.txt_67.text = puzzle2[67]
        self.txt_68.text = puzzle2[68]
        self.txt_69.text = puzzle2[69]
        self.txt_70.text = puzzle2[70]
        self.txt_71.text = puzzle2[71]
        self.txt_72.text = puzzle2[72]
        self.txt_73.text = puzzle2[73]
        self.txt_74.text = puzzle2[74]
        self.txt_75.text = puzzle2[75]
        self.txt_76.text = puzzle2[76]
        self.txt_77.text = puzzle2[77]
        self.txt_78.text = puzzle2[78]
        self.txt_79.text = puzzle2[79]
        self.txt_80.text = puzzle2[80]

class SudApp(App):
    def build(self):
        game = MyFirstWidget()
        return game
if __name__ == '__main__':
    SudApp().run()