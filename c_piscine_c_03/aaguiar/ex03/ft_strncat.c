/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aaguiar <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/16 21:10:41 by aaguiar           #+#    #+#             */
/*   Updated: 2019/10/17 12:39:25 by aaguiar          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

char	*ft_strncat(char *dest, char *src, unsigned int nb)
{
	int				z;
	unsigned int	x;

	z = 0;
	x = 0;
	while (dest[z] != '\0')
		z++;
	while (src[x] != '\0' && x < nb)
	{
		dest[z] = src[x];
		z++;
		x++;
	}
	dest[z] = '\0';
	return (dest);
}
