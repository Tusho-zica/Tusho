/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lkawachi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/16 21:22:07 by lkawachi          #+#    #+#             */
/*   Updated: 2019/10/16 22:05:02 by lkawachi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int ft_strncmp(char *s1, char *s2, unsigned int n)
{
	unsigned int x;

	x = 0;
	if (s1[x] == '\0' || s2[x] == '\0')
	{
		return (0);
	}
	while ((s1[x] != 0) && (x < (n - 1)))
	{
		x++;
	}
	return (s1[x] - s2[x]);
}

#include <stdio.h>
#include <string.h>

int main()
{
	printf("\n*** ex01 ***\n");
	{
		{
			char s0[] = "";
			char s1[] = "a";

			printf("\nOriginal strncmp: \"%d\" | ft_strncmp: \"%d\"\n", strncmp(s0,s1, 0), ft_strncmp(s0,s1, 0));
		}

		{
			char s0[] = "";
			char s1[] = "";

			printf("\nOriginal strncmp: \"%d\" | ft_strncmp: \"%d\"\n", strncmp(s0,s1, 0), ft_strncmp(s0,s1, 0));
		}


		{
			char s0[] = "12367";
			char s1[] = "12345";

			printf("\n Original strncmp: \"%d\" | ft_strncmp: \"%d\"\n", strncmp(s0,s1, 3), ft_strncmp(s0,s1, 3));
		}

		{
			char s0[] = "12367";
			char s1[] = "12345";

			printf("\nOriginal strncmp: \"%d\" | ft_strncmp: \"%d\"\n", strncmp(s0,s1, 4), ft_strncmp(s0,s1, 4));
		}

    {
			char s0[] = "123";
			char s1[] = "1230";

			printf("\nOriginal strncmp: \"%d\" | ft_strncmp: \"%d\"\n", strncmp(s0,s1, 4), ft_strncmp(s0,s1, 4));
		}

	}
}
