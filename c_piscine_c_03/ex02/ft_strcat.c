/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcat.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lkawachi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/16 22:14:47 by lkawachi          #+#    #+#             */
/*   Updated: 2019/10/16 22:38:31 by lkawachi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char *ft_strcat(char *dest, char *src)
{
	int x;
	int y;

	x = 0;
	y = 0;
	while (dest[x] != '\0')
	{
		x++;
	}
	while (src[y] != '\0')
	{
		dest[x] = src[y];
		x++;
		y++;
	}
	dest[x] = '\0';
	return (dest);
}

#include <stdio.h>
#include <string.h>

int main()
{
	printf("\n*** ex02 ***\n");
    {
		{
			char s1[] = "HELLOWORLD";
			char s11[] = "HELLOWORLD";
			char s2[] = "1234";

			s1[4] = 0;
			s11[4] = 0;
			printf("\nOriginal strncat: \"%s\" | ft_strncat: \"%s\"\n", strcat(s1,s2), ft_strcat(s11,s2));
		}

		{
			char s1[] = "HELLOWORLD";
			char s11[] = "HELLOWORLD";
			char s2[] = "";

			s1[4] = 0;
			s11[4] = 0;
			printf("\nOriginal strncat: \"%s\" | ft_strncat: \"%s\"\n", strcat(s1,s2), ft_strcat(s11,s2));
		}

		{
			char s1[] = "HELLOWORLD";
			char s11[] = "HELLOWORLD";
			char s2[] = "hello";

			s1[4] = 0;
			s11[4] = 0;
			printf("\nOriginal strncat: \"%s\" | ft_strncat: \"%s\"\n", strcat(s1,s2), ft_strcat(s11,s2));
		}
    }
}

