#A Escala de Magnitude de Momento (abreviada como MMS e denotada como Mw), introduzida em 1979
#por Thomas Haks e Hiroo Kanamori, substituiu a Escala de Richter para medir a magnitude dos terremotos
#em termos de energia liberada. Menos conhecida pelo público, a MMS é, no entanto, a escala usada para
#estimar as magnitudes de todos os grandes terremotos da atualidade. Assim como a escala Richter, a MMS
#é uma escala logarítmica. Mw e Mo se relacionam pela fórmula:
#Onde Mo é o momento sísmico (usualmente estimado a partir dos registros de movimento da superfície,
#através dos sismogramas), cuja unidade é o dina·cm. O terremoto de Kobe, acontecido no dia 17 de janeiro
#de 1995, foi um dos terremotos que causaram maior impacto no Japão e na comunidade científica
#internacional. Teve magnitude Mw = 7,3. Mostrando que é possível determinar a medida por meio de
#conhecimentos matemáticos, qual foi o momento sísmico Mo do terremoto de Kobe (em dina.cm).

# Magnitude do terremoto (Mw)
Mw = 7.3

# Fórmula para calcular o momento sísmico (Mo)
Mo = 10**(1.5 * Mw + 9.05)

# Saída do momento sísmico em dina·cm
print("O momento sísmico do terremoto de Kobe foi aproximadamente {:.2e} dina·cm.".format(Mo))



