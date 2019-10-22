/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_reverse_alphabet.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: lkawachi <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/06 18:45:42 by lkawachi          #+#    #+#             */
/*   Updated: 2019/10/06 19:00:37 by lkawachi         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char a)
{
	write(1, &a, 1);
}

void	ft_print_reverse_alphabet(void)
{
	char a;

	a = 'z';
	while (a >= 'a')
	{
		ft_putchar(a);
		a--;
	}
}
