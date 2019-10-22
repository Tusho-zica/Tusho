/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lkawachi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/16 19:47:50 by lkawachi          #+#    #+#             */
/*   Updated: 2019/10/16 21:21:13 by lkawachi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int ft_strcmp(char *s1, char *s2)
{
	int x;

	x = 0;
	while (s1[x] != '\0' && s1[x] == s2[x])
	{
		x++;
	}
	return (s1[x] - s2[x]);
}

#include <stdio.h>
#include <string.h>//necessário para strcmp
int main (void)
{
  char str1[4] = "abx";
  char str2[4] = "abc";
  int retorno;

  retorno = strcmp(str1, str2);
  printf("retorno = %d\n", retorno);
  //mostra o retorno da função strcmp

  return 0;
}
