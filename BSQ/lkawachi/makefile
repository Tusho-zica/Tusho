# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lkawachi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/22 11:41:08 by lkawachi          #+#    #+#              #
#    Updated: 2019/10/22 11:41:30 by lkawachi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


SRCS		= main.c

OBJS		= ${SRCS:.c=.o}

NAME		= bsq

CC			= cc

RM			= rm -f

CFLAGS		= -Wall -Werror -Wextra

.c.o:
	${CC} ${CFLAGS} -c $< -o ${<:.c=.o}

${NAME}:	${OBJS}
			${CC} -o ${NAME} ${OBJS}

all:		${Name}

clean:
			${RM} ${OBJS}

fclean:		clean
			${RM} ${NAME}
