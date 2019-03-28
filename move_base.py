import rospy 					#Biblioteca do ROS pra Python
from geometry_msgs.msg import Twist		#Node(eu acho) das mensagens que é responsavel pelas movimentações do turtle, o Twist, dentro dele que estão as variaveis de velocidades!

vel = Twist()					#Define "vel" como atalho para a função Twist() 
rospy.init_node("teste")			#Inicia um Node para esse codigo (Coisas do ROS que ainda não sei bem, mas pra esse codigo não é necessario por enquanto!
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10) #Define o publisher, ele que envia todas modificações feitas nas variaveis para o robo! 
#Se não publicar, o valor alterado não é aplicado no robo!
#Pelo que entendi, o Queue = 10 significa que ele armazena até 10 modificações pra enviar, algo do tipo


while not rospy.is_shutdown():  #Enquanto o rospy não for encerrado roda o codigo (Tipo o main desse codigo)
	#Ele ta só andando pra frente com a velocidade linear X de 1
	vel.linear.x = 1.0	#Velocidade Linear X
	vel.linear.y = 0.0	#Velocidade Linear Y
	vel.linear.z = 0.0	#Velocidade Linear Z
        #tem que descobrir o limite dessas velocida
	vel.angular.x = 0.0	#Velocidade Angular X
	vel.angular.y = 0.0	#Velocidade Angular Y
	vel.angular.z = 0.0	#Velocidade Angular Z
        
        pub.publish(vel)	#Publica todas as modificações

