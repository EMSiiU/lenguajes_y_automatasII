	.file	"prueba3.c"
	.text
	.globl	mayor
	.def	mayor;	.scl	2;	.type	32;	.endef
	.seh_proc	mayor
mayor:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	.seh_endprologue
	movl	%ecx, 16(%rbp)
	movl	%edx, 24(%rbp)
	movl	16(%rbp), %eax
	cmpl	24(%rbp), %eax
	jle	.L2
	movl	16(%rbp), %eax
	jmp	.L3
.L2:
	movl	24(%rbp), %eax
.L3:
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (Rev5, Built by MSYS2 project) 16.1.0"
