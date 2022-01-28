{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "854bd9df-a3d5-4773-ac22-7fda49653e92",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\fatim\\anaconda3\\lib\\site-packages (1.3.4)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\fatim\\anaconda3\\lib\\site-packages (from pandas) (2021.3)\n",
      "Requirement already satisfied: numpy>=1.17.3 in c:\\users\\fatim\\anaconda3\\lib\\site-packages (from pandas) (1.20.3)\n",
      "Requirement already satisfied: python-dateutil>=2.7.3 in c:\\users\\fatim\\anaconda3\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\fatim\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7.3->pandas) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "pd.__version__\n",
    "!pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "7cc409f6-bdf6-41d8-9240-7483c4166854",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    10\n",
      "1    20\n",
      "2    10\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "s1 = pd.Series([10, 20,10])\n",
    "print(s1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "043ff5dd-b6cc-420b-a939-4b8d5015030e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0     Rojo\n",
      "1    Verde\n",
      "2     Azul\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "s2 = pd.Series(['Rojo','Verde','Azul'])\n",
    "print(s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "afb4cc18-4a5e-4a9e-9c89-146929d9a0fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Número Objeto\n",
      "0      10   Rojo\n",
      "1      20  Verde\n",
      "2      10   Azul\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "s1 = pd.Series([10, 20,10])\n",
    "s2 = pd.Series(['Rojo','Verde','Azul'])\n",
    "\n",
    "df = pd.DataFrame({'Número':s1 ,\n",
    "                   'Objeto':s2})\n",
    "\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "05ac2bd3-ee3b-4c93-b7ff-98aa753b6e7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                                 URL  \\\n",
      "0      http://marvel.wikia.com/Henry_Pym_(Earth-616)   \n",
      "1  http://marvel.wikia.com/Janet_van_Dyne_(Earth-...   \n",
      "2  http://marvel.wikia.com/Anthony_Stark_(Earth-616)   \n",
      "3  http://marvel.wikia.com/Robert_Bruce_Banner_(E...   \n",
      "4   http://marvel.wikia.com/Thor_Odinson_(Earth-616)   \n",
      "\n",
      "                        nombre  n_apariciones actual  genero  fecha_inicio  \\\n",
      "0    Henry Jonathan \"Hank\" Pym           1269    YES    MALE          1963   \n",
      "1               Janet van Dyne           1165    YES  FEMALE          1963   \n",
      "2  Anthony Edward \"Tony\" Stark           3068    YES    MALE          1963   \n",
      "3          Robert Bruce Banner           2089    YES    MALE          1963   \n",
      "4                 Thor Odinson           2402    YES    MALE          1963   \n",
      "\n",
      "                                               Notes  \n",
      "0  Merged with Ultron in Rage of Ultron Vol. 1. A...  \n",
      "1  Dies in Secret Invasion V1:I8. Actually was se...  \n",
      "2  Death: \"Later while under the influence of Imm...  \n",
      "3  Dies in Ghosts of the Future arc. However \"he ...  \n",
      "4  Dies in Fear Itself brought back because that'...  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "vengadores = pd.read_csv('avengers.csv')\n",
    "fin= vengadores.head(5)\n",
    "print(fin)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ed8d06a0-0e87-4c3c-be3e-0e2753284ef1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                                 URL  \\\n",
      "0      http://marvel.wikia.com/Henry_Pym_(Earth-616)   \n",
      "1  http://marvel.wikia.com/Janet_van_Dyne_(Earth-...   \n",
      "2  http://marvel.wikia.com/Anthony_Stark_(Earth-616)   \n",
      "3  http://marvel.wikia.com/Robert_Bruce_Banner_(E...   \n",
      "4   http://marvel.wikia.com/Thor_Odinson_(Earth-616)   \n",
      "5  http://marvel.wikia.com/Richard_Jones_(Earth-616)   \n",
      "6  http://marvel.wikia.com/Steven_Rogers_(Earth-616)   \n",
      "7   http://marvel.wikia.com/Clint_Barton_(Earth-616)   \n",
      "8  http://marvel.wikia.com/Pietro_Maximoff_(Earth...   \n",
      "9  http://marvel.wikia.com/Wanda_Maximoff_(Earth-...   \n",
      "\n",
      "                        nombre  n_apariciones actual  genero  fecha_inicio  \\\n",
      "0    Henry Jonathan \"Hank\" Pym           1269    YES    MALE          1963   \n",
      "1               Janet van Dyne           1165    YES  FEMALE          1963   \n",
      "2  Anthony Edward \"Tony\" Stark           3068    YES    MALE          1963   \n",
      "3          Robert Bruce Banner           2089    YES    MALE          1963   \n",
      "4                 Thor Odinson           2402    YES    MALE          1963   \n",
      "5       Richard Milhouse Jones            612    YES    MALE          1963   \n",
      "6                Steven Rogers           3458    YES    MALE          1964   \n",
      "7       Clinton Francis Barton           1456    YES    MALE          1965   \n",
      "8              Pietro Maximoff            769    YES    MALE          1965   \n",
      "9               Wanda Maximoff           1214    YES  FEMALE          1965   \n",
      "\n",
      "                                               Notes  \n",
      "0  Merged with Ultron in Rage of Ultron Vol. 1. A...  \n",
      "1  Dies in Secret Invasion V1:I8. Actually was se...  \n",
      "2  Death: \"Later while under the influence of Imm...  \n",
      "3  Dies in Ghosts of the Future arc. However \"he ...  \n",
      "4  Dies in Fear Itself brought back because that'...  \n",
      "5                                                NaN  \n",
      "6    Dies at the end of Civil War. Later comes back.  \n",
      "7  Dies in exploding Kree ship in Averngers Vol. ...  \n",
      "8  Dies in House of M Vol 1 Issue 7. Later comes ...  \n",
      "9  Dies in Uncanny_Avengers_Vol_1_14. Later comes...  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "vengadores = pd.read_csv('avengers.csv')\n",
    "fin= vengadores.head(10)\n",
    "print(fin)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d0d03834-93fd-40cd-b287-b83b4dc980da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                                   URL          nombre  \\\n",
      "163  http://marvel.wikia.com/Tony_Masters_(Earth-616)#    Tony Masters   \n",
      "164  http://marvel.wikia.com/Victor_Mancha_(Earth-6...   Victor Mancha   \n",
      "165  http://marvel.wikia.com/Monica_Chang_(Earth-616)#    Monica Chang   \n",
      "166  http://marvel.wikia.com/Doombot_(Avenger)_(Ear...             NaN   \n",
      "167        http://marvel.wikia.com/Alexis_(Earth-616)#          Alexis   \n",
      "168   http://marvel.wikia.com/Eric_Brooks_(Earth-616)#     Eric Brooks   \n",
      "169  http://marvel.wikia.com/Adam_Brashear_(Earth-6...   Adam Brashear   \n",
      "170  http://marvel.wikia.com/Victor_Alvarez_(Earth-...  Victor Alvarez   \n",
      "171     http://marvel.wikia.com/Ava_Ayala_(Earth-616)#       Ava Ayala   \n",
      "172         http://marvel.wikia.com/Kaluu_(Earth-616)#           Kaluu   \n",
      "\n",
      "     n_apariciones actual  genero  fecha_inicio  \\\n",
      "163            173     NO    MALE          2013   \n",
      "164             75    YES    MALE          2013   \n",
      "165             12    YES  FEMALE          2013   \n",
      "166             14    YES    MALE          2013   \n",
      "167             13    YES  FEMALE          2013   \n",
      "168            198    YES    MALE          2013   \n",
      "169             29    YES    MALE          2014   \n",
      "170             45    YES    MALE          2014   \n",
      "171             49    YES  FEMALE          2014   \n",
      "172             35    YES    MALE          2015   \n",
      "\n",
      "                                                 Notes  \n",
      "163                                                NaN  \n",
      "164  Died in Avengers_A.I._Vol_1_4. Returned in Ave...  \n",
      "165                                                NaN  \n",
      "166                                                NaN  \n",
      "167                                                NaN  \n",
      "168                                                NaN  \n",
      "169                                                NaN  \n",
      "170                                                NaN  \n",
      "171                                                NaN  \n",
      "172                                                NaN  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "vengadores = pd.read_csv('avengers.csv')\n",
    "fin= vengadores.tail(10)\n",
    "print(fin)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "60f286d6-d411-4fc2-b920-762f879e0d56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "173\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "vengadores = pd.read_csv('avengers.csv')\n",
    "fin= len(vengadores.index)\n",
    "print(fin)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9e5298a9-616f-4a5b-be0a-c9c64f153f29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                                            URL  \\\n",
      "fecha_inicio                                                      \n",
      "1963              http://marvel.wikia.com/Henry_Pym_(Earth-616)   \n",
      "1963          http://marvel.wikia.com/Janet_van_Dyne_(Earth-...   \n",
      "1963          http://marvel.wikia.com/Anthony_Stark_(Earth-616)   \n",
      "1963          http://marvel.wikia.com/Robert_Bruce_Banner_(E...   \n",
      "1963           http://marvel.wikia.com/Thor_Odinson_(Earth-616)   \n",
      "...                                                         ...   \n",
      "2013           http://marvel.wikia.com/Eric_Brooks_(Earth-616)#   \n",
      "2014          http://marvel.wikia.com/Adam_Brashear_(Earth-6...   \n",
      "2014          http://marvel.wikia.com/Victor_Alvarez_(Earth-...   \n",
      "2014             http://marvel.wikia.com/Ava_Ayala_(Earth-616)#   \n",
      "2015                 http://marvel.wikia.com/Kaluu_(Earth-616)#   \n",
      "\n",
      "                                   nombre  n_apariciones actual  genero  \\\n",
      "fecha_inicio                                                              \n",
      "1963            Henry Jonathan \"Hank\" Pym           1269    YES    MALE   \n",
      "1963                       Janet van Dyne           1165    YES  FEMALE   \n",
      "1963          Anthony Edward \"Tony\" Stark           3068    YES    MALE   \n",
      "1963                  Robert Bruce Banner           2089    YES    MALE   \n",
      "1963                         Thor Odinson           2402    YES    MALE   \n",
      "...                                   ...            ...    ...     ...   \n",
      "2013                          Eric Brooks            198    YES    MALE   \n",
      "2014                        Adam Brashear             29    YES    MALE   \n",
      "2014                       Victor Alvarez             45    YES    MALE   \n",
      "2014                            Ava Ayala             49    YES  FEMALE   \n",
      "2015                                Kaluu             35    YES    MALE   \n",
      "\n",
      "                                                          Notes  \n",
      "fecha_inicio                                                     \n",
      "1963          Merged with Ultron in Rage of Ultron Vol. 1. A...  \n",
      "1963          Dies in Secret Invasion V1:I8. Actually was se...  \n",
      "1963          Death: \"Later while under the influence of Imm...  \n",
      "1963          Dies in Ghosts of the Future arc. However \"he ...  \n",
      "1963          Dies in Fear Itself brought back because that'...  \n",
      "...                                                         ...  \n",
      "2013                                                        NaN  \n",
      "2014                                                        NaN  \n",
      "2014                                                        NaN  \n",
      "2014                                                        NaN  \n",
      "2015                                                        NaN  \n",
      "\n",
      "[173 rows x 6 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "vengadores = pd.read_csv('avengers.csv')\n",
    "fin= vengadores.set_index('fecha_inicio')\n",
    "print(fin)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "48de7e57-9340-4be2-bae3-ef6b33b3b2e3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                                   URL          nombre  \\\n",
      "172         http://marvel.wikia.com/Kaluu_(Earth-616)#           Kaluu   \n",
      "157  http://marvel.wikia.com/Sam_Alexander_(Earth-6...   Sam Alexander   \n",
      "171     http://marvel.wikia.com/Ava_Ayala_(Earth-616)#       Ava Ayala   \n",
      "170  http://marvel.wikia.com/Victor_Alvarez_(Earth-...  Victor Alvarez   \n",
      "169  http://marvel.wikia.com/Adam_Brashear_(Earth-6...   Adam Brashear   \n",
      "..                                                 ...             ...   \n",
      "123  http://marvel.wikia.com/Emery_Schaub_(Earth-616)#    Emery Schaub   \n",
      "122  http://marvel.wikia.com/James_Santini_(Earth-6...   James Santini   \n",
      "75   http://marvel.wikia.com/Elvin_Haliday_(Earth-6...   Elvin Haliday   \n",
      "76   http://marvel.wikia.com/William_Baker_(Earth-6...   William Baker   \n",
      "128   http://marvel.wikia.com/Julie_Power_(Earth-616)#     Julie Power   \n",
      "\n",
      "     n_apariciones actual  genero  fecha_inicio  \\\n",
      "172             35    YES    MALE          2015   \n",
      "157             78    YES    MALE          2015   \n",
      "171             49    YES  FEMALE          2014   \n",
      "170             45    YES    MALE          2014   \n",
      "169             29    YES    MALE          2014   \n",
      "..             ...    ...     ...           ...   \n",
      "123             26    YES    MALE          1900   \n",
      "122             40    YES    MALE          1900   \n",
      "75             158     NO    MALE          1900   \n",
      "76             355     NO    MALE          1900   \n",
      "128            153    YES  FEMALE          1900   \n",
      "\n",
      "                                                 Notes  \n",
      "172                                                NaN  \n",
      "157                                                NaN  \n",
      "171                                                NaN  \n",
      "170                                                NaN  \n",
      "169                                                NaN  \n",
      "..                                                 ...  \n",
      "123                                                NaN  \n",
      "122                                                NaN  \n",
      "75                                                 NaN  \n",
      "76   Died in Identity_Disc_Vol_1_1. Later was revea...  \n",
      "128                                                NaN  \n",
      "\n",
      "[173 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "vengadores = pd.read_csv('avengers.csv')\n",
    "fin= vengadores.set_index('fecha_inicio')\n",
    "con = vengadores.sort_values(by='fecha_inicio', ascending=False)\n",
    "print(con)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "70672675-1bfb-43d3-a964-d0757d7bfefb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     fecha_inicio                                                URL  \\\n",
      "0            1963      http://marvel.wikia.com/Henry_Pym_(Earth-616)   \n",
      "1            1963  http://marvel.wikia.com/Janet_van_Dyne_(Earth-...   \n",
      "2            1963  http://marvel.wikia.com/Anthony_Stark_(Earth-616)   \n",
      "3            1963  http://marvel.wikia.com/Robert_Bruce_Banner_(E...   \n",
      "4            1963   http://marvel.wikia.com/Thor_Odinson_(Earth-616)   \n",
      "..            ...                                                ...   \n",
      "168          2013   http://marvel.wikia.com/Eric_Brooks_(Earth-616)#   \n",
      "169          2014  http://marvel.wikia.com/Adam_Brashear_(Earth-6...   \n",
      "170          2014  http://marvel.wikia.com/Victor_Alvarez_(Earth-...   \n",
      "171          2014     http://marvel.wikia.com/Ava_Ayala_(Earth-616)#   \n",
      "172          2015         http://marvel.wikia.com/Kaluu_(Earth-616)#   \n",
      "\n",
      "                          nombre  n_apariciones actual  genero  \\\n",
      "0      Henry Jonathan \"Hank\" Pym           1269    YES    MALE   \n",
      "1                 Janet van Dyne           1165    YES  FEMALE   \n",
      "2    Anthony Edward \"Tony\" Stark           3068    YES    MALE   \n",
      "3            Robert Bruce Banner           2089    YES    MALE   \n",
      "4                   Thor Odinson           2402    YES    MALE   \n",
      "..                           ...            ...    ...     ...   \n",
      "168                  Eric Brooks            198    YES    MALE   \n",
      "169                Adam Brashear             29    YES    MALE   \n",
      "170               Victor Alvarez             45    YES    MALE   \n",
      "171                    Ava Ayala             49    YES  FEMALE   \n",
      "172                        Kaluu             35    YES    MALE   \n",
      "\n",
      "                                                 Notes  \n",
      "0    Merged with Ultron in Rage of Ultron Vol. 1. A...  \n",
      "1    Dies in Secret Invasion V1:I8. Actually was se...  \n",
      "2    Death: \"Later while under the influence of Imm...  \n",
      "3    Dies in Ghosts of the Future arc. However \"he ...  \n",
      "4    Dies in Fear Itself brought back because that'...  \n",
      "..                                                 ...  \n",
      "168                                                NaN  \n",
      "169                                                NaN  \n",
      "170                                                NaN  \n",
      "171                                                NaN  \n",
      "172                                                NaN  \n",
      "\n",
      "[173 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "vengadores = pd.read_csv('avengers.csv')\n",
    "fin= vengadores.set_index('fecha_inicio')\n",
    "con = vengadores.sort_values(by='fecha_inicio', ascending=False)\n",
    "inicial = fin.reset_index()\n",
    "print(inicial)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93b87391-c0e6-4425-9822-a4a82651b2a0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
