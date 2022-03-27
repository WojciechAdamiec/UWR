	.text
	.globl	bitrev
	.type	bitrev, @function

bitrev: # Input: %rdi
	
	mov %rdi, %rax                       # 64/32/16 Block

	rol $8,  %ax
	rol $16, %eax
	rol $8,  %ax

	shr $32, %rdi
	rol $8,  %di 
	rol $16, %edi
	rol $8,  %di

	shl $32, %rax 
	or %rdi,%rax
	mov %rax, %rdi

	movabsq $0x0F0F0F0F0F0F0F0F, %r10    # 8 Block
	shr $4, %rdi
	and %r10, %rdi
	and %r10, %rax
	shl $4, %rax
	or  %rdi, %rax
	mov %rax, %rdi

	movabsq $0x3333333333333333, %r10    # 4 Block
	shr $2, %rdi
	and %r10, %rdi
	and %r10, %rax
	shl $2, %rax
	or  %rdi, %rax
	mov %rax, %rdi

	movabsq $0x5555555555555555, %r10    # 2 Block
	shr $1, %rdi
	and %r10, %rdi
	and %r10, %rax
	shl $1, %rax
	or  %rdi, %rax

	ret # Output: %rax

	.size	bitrev, .-bitrev