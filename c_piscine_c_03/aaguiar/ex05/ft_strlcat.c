/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: aaguiar <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2019/10/17 08:50:51 by aaguiar           #+#    #+#             */
/*   Updated: 2019/10/17 08:59:37 by aaguiar          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

unsigned int	ft_strlcat(char *dest, char *src, unsigned int size)
{
	unsigned int z;
	unsigned int x;
	unsigned int res;

	z = 0;
	while (dest[z] != '\0')
		++z;
	res = 0;
	while (src[res] != '\0')
		++res;
	if (size <= z)
		res += size;
	else
		res += z;
	x = 0;
	while (src[x] != '\0' && z + 1 < size)
	{
		dest[z] = src[x];
		z++;
		x++;
	}
	dest[z] = '\0';
	return (res);
}
